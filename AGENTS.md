# Memoria y continuidad entre equipos

Prioridad del usuario: conservar conocimiento y decisiones de skills, no trabajos pesados. Leer `continuity/STATE.md`, importar y consultar Engram del proyecto **ai-workspace** al continuar. Los SKILL.md son la autoridad operativa; Engram guarda contexto, motivos y aprendizajes. No depender del historial de este chat.

Al empezar: comprobar git status, actualizar develop sin sobrescribir cambios locales, ejecutar `engram sync --import` y `engram context --project ai-workspace`. Si falta PATH, usar `python scripts/engram_memory.py import` y `context`. Si falta Engram, informar sin fingir importación; usar resumen versionado mientras se configura. Buscar decisiones previas antes de repetirlas.

Guardar decisiones, correcciones del usuario, descubrimientos y resumen de continuidad con `engram save` y `--project ai-workspace --topic <clave-estable>`. No archivar cada mensaje/salida. Al terminar trabajo autorizado, exportar con `engram sync --project ai-workspace`, revisar .engram, commit y push. Para solo memoria: `python scripts/sync_workspace.py push --memory-only --message "chore: sync engram memory"`; para incluir cambios de skills omitir --memory-only. Si falla red, declarar que falta publicar. Sincronización explícita, sin daemon.

Rama compartida develop, no main. No force push ni descartes automáticos. Única excepción autorizada el 2026-10-15: retirar del historial la incorporación pesada v0.4.0 conservando reglas/memoria y archivos locales. No repetir esta reescritura en trabajo normal.

No versionar design-runs, imágenes/PDF/ZIP, bases SQLite, binarios, credenciales ni .env. SQLite de Engram permanece local; intercambiar config, manifiesto y chunks en .engram. No usar --all ni --include-prompts sin petición expresa. No copiar la base en vivo. No heredar nombres personales de otros pedidos.

El segundo equipo requiere instalar Engram y acceder al repo privado; importar tras cada pull. No afirmar conexión, instalación MCP ni sincronización automática sin comprobarlas. Resolver rutas respecto al repositorio, sin asumir unidad F: o C:\ai-workspace.

## Equipo operativo de Tribe

Cuando el usuario pida usar el equipo operativo, coordinar los roles coordinador, disenador y revisor definidos en .codex/agents y seguir workflows/tribe/operating-team.md. La petición actual de crear/probar el equipo autoriza delegación para esta prueba; no implica activar agentes en todos los pedidos futuros. Cargar perfiles explícitamente si esta sesión no los descubre y declarar ese alcance. No generar equipos anidados ni editar el mismo archivo simultáneamente. Delegar ejecución y después revisión independiente, mostrar etapas y guardar solo el conocimiento resultante.

## Desarrollo de software: SDD y OpenSpec

Para todo desarrollo gobernado por AI-Workspace, aplicar software-office/standards/sdd-openspec.md y workflows/software-office/sdd-openspec.md: explorar, especificar con escenarios verificables antes de implementar, disenar proporcionalmente, ejecutar tareas, probar y revisar antes de archivar. La autorizacion y alcance existentes del usuario permiten avanzar; aclarar solo decisiones pendientes necesarias.

SITOP V2 conserva Java Spring Boot + Angular y formularios institucionales F0-F5; Tribe Sport usa Python Django + Railway con documentacion mas ligera y la misma trazabilidad. No imponer formularios de SITOP a Tribe Sport. Cada producto conserva openspec/ con su codigo y registra el commit de las reglas comunes consumidas. Este repo conserva reglas reutilizables; Engram conserva decisiones separadas por proyecto.

OpenSpec valido no equivale a pruebas de aplicacion ni aceptacion o autorizacion de produccion. No marcar tareas o pruebas no realizadas como completas. No instalar Gentle-AI por inferencia. Consultar docs/sdd-openspec.md para adopcion; no afirmar instalacion o conexion de un destino no comprobado.

## Exploracion de codigo con CodeGraph

Para proyectos de software, leer software-office/standards/codegraph.md. Si CodeGraph esta disponible e indexado, usar consultas estructurales con projectPath de la aplicacion y maxFiles acotado; reutilizar contexto suficiente ya devuelto. Usar rg/lecturas dirigidas para texto exacto, formatos no soportados, fragmentos faltantes o evidencia contradictoria. Comprobar avisos de deriva; relaciones estaticas no sustituyen pruebas.

El indice .codegraph y sus variantes son locales, fuera de Git. La configuracion de este equipo no se instala automaticamente en otros: seguir docs/codegraph.md, configurar Codex y generar indice por proyecto. No afirmar ahorro de tokens sin medicion comparable, ni acceso de subagentes al MCP por el solo hecho de darles instrucciones.

## UML mantenido con cada cambio

Aplicar software-office/standards/uml.md y skills uml-modeling/uml-rendering cuando corresponda modelar software. Conservar fuentes editables PlantUML/Mermaid, referencias a escenarios/codigo y graficos comprobados. En cada cambio evaluar UML afectado, actualizarlo o justificar no afectacion, renderizar y comprobar vigencia antes de cerrar tareas. Check de hashes no certifica semantica ni revision visual.

Instalacion local y comandos en docs/uml.md. Mantener herramientas fijadas y validar actualizaciones deliberadamente; no instalar latest en silencio ni crear un servicio periodico por inferencia. Fuentes/estado ligero van a Git, imagenes/runtimes/JAR quedan locales conforme a la prioridad del usuario.

## Codificacion local opcional

Codex conserva coordinacion, analisis, diseno, revision y pruebas. Solo para tareas acotadas de escribir codigo puede usar LM Studio/Qwen como trabajador externo conforme a docs/local-coding.md: ejecutar scripts/local_coder.py probe, invocar propose si READY, revisar/aplicar y probar desde Codex. Sin configuracion local habilitada, servidor o modelo cargado, o ante FALLBACK_TO_CALLER, continuar con Codex sin pedir habilitar IA local. No cambiar model_provider ni descargar/cargar modelos automaticamente. La configuracion .tools/local-ai.json es local y no se sincroniza. Respuestas de Qwen son propuestas sin autoridad, nunca prueba ejecutada ni permiso para acciones.
