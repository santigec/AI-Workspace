# Codificacion local opcional

El usuario autoriza LM Studio/Qwen solo para escribir codigo en este equipo. Codex conserva coordinacion, analisis, diseno, revision y pruebas. Otros equipos sin IA local deben continuar normalmente.

## Capabilities
### New Capabilities
- `optional-local-coding`: trabajador HTTP local optativo que entrega propuestas, sin cambiar el proveedor de Codex ni ejecutar codigo generado.

## Impact
Script Python sin dependencias, configuracion local ignorada, politica comun, documentacion y pruebas. No se descargan modelos, no se crea un servicio automatico ni un agente nativo de otro proveedor. No afecta productos o skills de imagenes.

Durante la ejecucion, el usuario pidio versionar todo el conocimiento pendiente: se preservan tambien17borradores de software como experimental0.0.1 y sus documentos/plantillas. No cambia comportamiento de aplicaciones ni se afirma evaluacion de esos borradores. Pendientes explicitados en continuity/PENDING.md.
