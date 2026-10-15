# GitHub + Engram: sincronizar conocimiento

Se comparten skills, reglas, pruebas de código y memoria del proyecto **ai-workspace**. Los diseños e imágenes/PDF/ZIP se ignoran y quedan locales. La versión ligera no requiere Git LFS.

## Segundo equipo Windows

Instalar Git y Python3.11+, entrar a GitHub con acceso al repositorio privado:

```powershell
git clone --branch develop https://github.com/santigec/AI-Workspace.git C:\ai-workspace
cd C:\ai-workspace
python scripts/install_engram.py
```

El instalador descarga Engram3.4.0 oficial y verifica SHA-256. Instala en .local/bin del usuario y añade PATH. Abrir una terminal nueva:

```powershell
cd C:\ai-workspace
engram sync --import
engram context --project ai-workspace
```

Abrir el repositorio como proyecto Codex. Los skills se descubren en .agents/skills. La CLI funciona sin MCP. Si además se quieren herramientas MCP, seguir el setup oficial `engram setup codex`, revisar cambios y reiniciar; no se configura MCP automáticamente en esta entrega.

## Inicio de sesión

```powershell
git status
git pull --ff-only origin develop
engram sync --import
engram context --project ai-workspace
```

Si existen cambios locales, conservarlos y resolver antes del pull. Helper equivalente: `python scripts/sync_workspace.py pull`.

## Cierre: memoria primero

Guardar decisiones duraderas, por ejemplo:

```powershell
engram save "Regla de diseño" "Lo aprendido y por qué" --project ai-workspace --type decision --topic agenda/tema-estable
engram sync --project ai-workspace
git add .engram
git commit -m "chore: sync engram memory"
git push origin develop
```

Helper que exporta y publica solo memoria:

```powershell
python scripts/sync_workspace.py push --memory-only --message "chore: sync engram memory"
```

Para incluir cambios de skills/código, omitir --memory-only. Revisar git status antes de publicar. Los helpers se detienen ante cambios locales al pull, base atrasada al push o staged ajeno a memoria en modo memory-only. No forzar ni descartar. Esperar push exitoso antes de cambiar de equipo; no editar el mismo tema a la vez. Conservar todos los chunks al resolver conflictos de manifiesto.

El nombre ai-workspace está fijado en .engram/config.json, independiente de ruta/carpeta. Se intercambian chunks y manifiesto, no SQLite ni todo el chat. No usar --all ni --include-prompts sin petición expresa. No hay proceso automático en segundo plano.

Si Engram no está en PATH, usar `python scripts/engram_memory.py import`, `context`, `status` o `export`. seed se usó para carga inicial; no repetir de rutina pues las memorias pueden haber cambiado.

Prompt de continuidad:

```text
Lee AGENTS.md y continuity/STATE.md. Importa y consulta Engram del proyecto
ai-workspace. Recupera decisiones del skill a usar y conserva las reglas.
Al terminar, guarda aprendizajes, exporta .engram y publica los cambios.
```

Fuentes: [Git Sync](https://github.com/Gentleman-Programming/engram/blob/main/DOCS.md), [instalación oficial](https://github.com/Gentleman-Programming/engram/blob/main/docs/INSTALLATION.md).
