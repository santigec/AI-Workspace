## Context

La oficina usa SDD/OpenSpec y Engram. AI-Workspace tiene un runtime Node y herramientas locales; los proyectos de aplicacion viven en repos separados. El usuario autoriza instalar CodeGraph para su uso comun. Se identifica la variante @colbymchenry/codegraph por su integracion explicita en Gentleman-Programming/gentle-ai, evitando confundir proyectos homonimos.

## Goals / Non-Goals

Instalacion reproducible, MCP verificado, exploracion acotada y reglas compartidas. No migrar codigo, instalar Gentle-AI, indexar discos completos, medir ahorro sin datos ni versionar bases.

## Decisions

- Usar dependencia local fijada y lockfile; comando MCP resuelto a rutas absolutas solo en la configuracion local de cada maquina.
- Servir navegacion del codigo, sin herramientas de edicion o ejecucion arbitraria. Los indices pueden escribirse localmente como parte del funcionamiento del servidor.
- Verificar CLI, exclusion del indice, consulta con MCP y actualizacion del indice tras un cambio sintetico. Los proyectos reales no disponibles se documentan como pendientes.
- Mantener politicas propias fuera de archivos generados del proveedor. No adoptar instrucciones upstream de confiar ciegamente en un indice o reemplazar pruebas por sus relaciones.
- No agregar un daemon personalizado; usar el comportamiento del proveedor y limitar MCP a los comandos pertinentes.

## Risks / Trade-offs

La presencia de una configuracion MCP no la carga en una conversacion ya abierta. El soporte de lenguaje y relaciones dinamicas es parcial: verificar casos afectados cuando importe. Un indice de codigo consume disco local y puede dar contexto incorrecto si esta atrasado. El ahorro depende de consulta, repo y contenido retornado; no se garantiza un porcentaje.

## Migration Plan

Instalar y verificar aqui, registrar la integracion en este Codex y publicar scripts/reglas. Al abrir cada aplicacion crear su indice una vez y comprobar projectPath y estado. En otro equipo ejecutar instalacion y configuracion locales despues del pull.

## Open Questions

Faltan rutas de SITOP y Tribe Sport y una medicion comparativa de tokens en tareas reales; no bloquean una instalacion y prueba acotadas.
