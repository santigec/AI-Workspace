"""Install pinned official Engram for Windows; verify SHA-256 before extracting."""
import hashlib
import io
import os
from pathlib import Path
import platform
import urllib.request
import zipfile

VERSION = '3.4.0'
HASHES = {
    'amd64': '3065736ec7ff8137eb3fc607275f542ea13bb743a5157318c8a8770f11ce3289',
    'arm64': '7463872a85a5e5434cf958bdffc71dda1926bced30d3b6b38c80fec9bb98fbba',
}

def install():
    if platform.system() != 'Windows':
        raise SystemExit('Use the official Engram installation for your OS: https://github.com/Gentleman-Programming/engram')
    arch = 'arm64' if platform.machine().lower() in ('arm64','aarch64') else 'amd64'
    filename = f'engram_{VERSION}_windows_{arch}.zip'
    url = f'https://github.com/Gentleman-Programming/engram/releases/download/v{VERSION}/{filename}'
    with urllib.request.urlopen(url, timeout=120) as response:
        data = response.read()
    if hashlib.sha256(data).hexdigest() != HASHES[arch]:
        raise SystemExit('SHA-256 mismatch. Nothing installed.')
    with zipfile.ZipFile(io.BytesIO(data)) as archive:
        members = [n for n in archive.namelist() if Path(n).name == 'engram.exe']
        if len(members) != 1:
            raise SystemExit('Unexpected archive layout. Nothing installed.')
        binary = archive.read(members[0])
    target = Path.home()/'.local/bin'
    target.mkdir(parents=True, exist_ok=True)
    (target/'engram.exe').write_bytes(binary)
    import winreg
    with winreg.CreateKey(winreg.HKEY_CURRENT_USER, 'Environment') as key:
        try:
            old,kind = winreg.QueryValueEx(key, 'Path')
        except FileNotFoundError:
            old,kind = '',winreg.REG_EXPAND_SZ
        if str(target).lower().rstrip('\\') not in [x.lower().rstrip('\\') for x in old.split(';')]:
            winreg.SetValueEx(key, 'Path', 0, kind, old.rstrip(';')+';'+str(target))
    print(f'Installed verified Engram {VERSION}: {target / "engram.exe"}')
    print('Open a new terminal for PATH; Python helpers can resolve this installation immediately.')

if __name__ == '__main__':
    install()
