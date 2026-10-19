# Memoria y continuidad entre equipos

Prioridad del usuario: conservar conocimiento y decisiones de skills, no trabajos pesados. Leer `continuity/STATE.md`, importar y consultar Engram del proyecto **ai-workspace** al continuar. Los SKILL.md son la autoridad operativa; Engram guarda contexto, motivos y aprendizajes. No depender del historial de este chat.

Al empezar: comprobar git status, actualizar develop sin sobrescribir cambios locales, ejecutar `engram sync --import` y `engram context --project ai-workspace`. Si falta PATH, usar `python scripts/engram_memory.py import` y `context`. Si falta Engram, informar sin fingir importación; usar resumen versionado mientras se configura. Buscar decisiones previas antes de repetirlas.

Guardar decisiones, correcciones del usuario, descubrimientos y resumen de continuidad con `engram save` y `--project ai-workspace --topic <clave-estable>`. No archivar cada mensaje/salida. Al terminar trabajo autorizado, exportar con `engram sync --project ai-workspace`, revisar .engram, commit y push. Para solo memoria: `python scripts/sync_workspace.py push --memory-only --message "chore: sync engram memory"`; para incluir cambios de skills omitir --memory-only. Si falla red, declarar que falta publicar. Sincronización explícita, sin daemon.

Rama compartida develop, no main. No force push ni descartes automáticos. Única excepción autorizada el 2026-10-15: retirar del historial la incorporación pesada v0.4.0 conservando reglas/memoria y archivos locales. No repetir esta reescritura en trabajo normal.

No versionar design-runs, imágenes/PDF/ZIP, bases SQLite, binarios, credenciales ni .env. SQLite de Engram permanece local; intercambiar config, manifiesto y chunks en .engram. No usar --all ni --include-prompts sin petición expresa. No copiar la base en vivo. No heredar nombres personales de otros pedidos.

El segundo equipo requiere instalar Engram y acceder al repo privado; importar tras cada pull. No afirmar conexión, instalación MCP ni sincronización automática sin comprobarlas. Resolver rutas respecto al repositorio, sin asumir unidad F: o C:\ai-workspace.

## Equipo operativo de Tribe

Cuando el usuario pida usar el equipo operativo, coordinar los roles coordinador, disenador y revisor definidos en .codex/agents y seguir workflows/tribe/operating-team.md. La petición actual de crear/probar el equipo autoriza delegación para esta prueba; no implica activar agentes en todos los pedidos futuros. Cargar perfiles explícitamente si esta sesión no los descubre y declarar ese alcance. No generar equipos anidados ni editar el mismo archivo simultáneamente. Delegar ejecución y después revisión independiente, mostrar etapas y guardar solo el conocimiento resultante.
