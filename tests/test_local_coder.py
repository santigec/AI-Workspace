"""Optional local worker boundaries and transport contract; no external model required."""
import importlib.util
import json
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('local_coder', ROOT / 'scripts/local_coder.py')
worker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(worker)


class WorkerTests(unittest.TestCase):
    def setUp(self):
        temp = tempfile.TemporaryDirectory(prefix='local-coder-test-', dir=ROOT.parent)
        assert Path(temp.name).resolve().is_relative_to(ROOT.parent.resolve())
        self.addCleanup(temp.cleanup)
        self.project = Path(temp.name).resolve()
        self.config = self.project / 'config.json'
        self.models = {'models': [{'key': 'qwen', 'type': 'llm',
                                  'loaded_instances': [{'id': 'loaded-qwen', 'config': {'context_length': 8192}}]}]}
        self.reply = {'choices': [{'finish_reason': 'stop', 'message': {'content': 'def add(a, b): return a + b'}}]}
        self.posts = []
        self.redirect = False
        owner = self

        class Handler(BaseHTTPRequestHandler):
            def log_message(self, *args):
                pass

            def do_GET(self):
                if owner.redirect:
                    self.send_response(302)
                    self.send_header('Location', 'http://example.com')
                    self.end_headers()
                    return
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(owner.models).encode())

            def do_POST(self):
                owner.posts.append(json.loads(self.rfile.read(int(self.headers['Content-Length']))))
                self.send_response(200)
                self.end_headers()
                self.wfile.write(json.dumps(owner.reply).encode())

        server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        thread = threading.Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(server.server_close)
        self.addCleanup(server.shutdown)
        self.config.write_text(json.dumps({'enabled': True, 'model': 'qwen',
                                          'base_url': f'http://127.0.0.1:{server.server_port}'}))

    def run_worker(self, task=None, files=None):
        return worker.run(self.config, self.project, task, files or [])

    def test_probe_ready_does_not_generate(self):
        self.assertEqual(self.run_worker()['status'], 'READY')
        self.assertEqual(self.posts, [])

    def test_missing_or_disabled_never_calls_network(self):
        self.config.unlink()
        with patch.object(worker.Client, 'call', side_effect=AssertionError('No network')):
            self.assertEqual(self.run_worker()['status'], 'FALLBACK_TO_CALLER')
            self.config.write_text('{"enabled": false}')
            self.assertEqual(self.run_worker()['status'], 'FALLBACK_TO_CALLER')

    def test_only_explicit_loaded_llm(self):
        self.models['models'][0]['loaded_instances'] = []
        self.assertEqual(self.run_worker('code')['status'], 'FALLBACK_TO_CALLER')
        self.assertEqual(self.posts, [])

    def test_proposal_is_not_applied(self):
        source = self.project / 'sample.py'
        source.write_text('before')
        result = self.run_worker('Implement add', ['sample.py'])
        self.assertEqual(result['status'], 'PROPOSAL_REQUIRES_REVIEW')
        self.assertFalse(result['applied'])
        self.assertFalse(result['tests_executed'])
        self.assertEqual(source.read_text(), 'before')
        self.assertEqual(self.posts[0]['model'], 'loaded-qwen')
        self.assertLessEqual(self.posts[0]['max_tokens'], 1024)

    def test_bad_context_rejected_before_post(self):
        (self.project / '.env').write_text('SECRET=private')
        (self.project / 'large.py').write_text('x' * (worker.MAX_INPUT + 1))
        for files in [['../outside.py'], ['.env'], ['large.py'], ['a'] * 6]:
            with self.subTest(files=files):
                self.assertEqual(self.run_worker('task', files)['status'], 'FALLBACK_TO_CALLER')
        self.assertEqual(self.posts, [])

    def test_budget_covers_task_plus_context(self):
        (self.project / 'ok.py').write_text('x' * 8000)
        self.assertEqual(self.run_worker('t' * 5000, ['ok.py'])['status'], 'FALLBACK_TO_CALLER')
        self.assertEqual(self.posts, [])

    def test_timeout_returns_control(self):
        with patch.object(worker.Client, 'call', side_effect=TimeoutError()):
            self.assertEqual(self.run_worker('task')['status'], 'FALLBACK_TO_CALLER')

    def test_invalid_and_truncated_generation(self):
        for reply in [{}, {'choices': []}, {'choices': [{'finish_reason': 'length',
                                                       'message': {'content': 'partial'}}]}]:
            self.reply = reply
            self.assertEqual(self.run_worker('task')['status'], 'FALLBACK_TO_CALLER')

    def test_nonlocal_urls_rejected(self):
        for url in ['http://192.168.1.2:1234', 'https://127.0.0.1:1234',
                    'http://user:password@127.0.0.1:1234', 'http://127.0.0.1:1234/path']:
            with self.subTest(url=url), self.assertRaises(ValueError):
                worker.Client(url)

    def test_redirect_not_followed(self):
        self.redirect = True
        self.assertEqual(self.run_worker()['status'], 'FALLBACK_TO_CALLER')
        self.assertEqual(self.posts, [])

    def test_malformed_models_fall_back(self):
        for models in [{'models': [None]}, {'models': None}, {}]:
            self.models = models
            self.assertEqual(self.run_worker()['status'], 'FALLBACK_TO_CALLER')


if __name__ == '__main__':
    unittest.main()
