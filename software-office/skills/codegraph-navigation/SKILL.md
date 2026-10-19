---
name: codegraph-navigation
description: Explora simbolos, flujos y dependencias de proyectos de software con CodeGraph local, contexto acotado, proyecto explicito y comprobacion de frescura del indice.
---

# Navegacion de codigo con CodeGraph

Usar cuando se necesite comprender codigo o impacto estructural en las oficinas de software. Leer [politica](../../standards/codegraph.md) y [guia de configuracion](../../../docs/codegraph.md). Se integra con [SDD/OpenSpec](../../standards/sdd-openspec.md); la inspeccion del comportamiento precede a su especificacion.

1. Identificar la aplicacion y su ruta accesible. Distinguir paquete instalado, MCP configurado y herramienta realmente cargada. No consultar por defecto el indice de AI-Workspace para responder sobre otra aplicacion.
2. Si el proyecto tiene indice, consultar `codegraph_explore` con projectPath y una pregunta que incluya archivo/simbolo cuando se conozcan. Empezar con maxFiles 1-5 segun la tarea. El CLI compartido permite explorar si MCP no esta disponible; ver comandos de la guia.
3. Reutilizar contexto suficiente ya retornado; no repetir lecturas completas. Atender truncado y avisos de deriva, completar solo partes relevantes con otra consulta o herramientas de archivos. Para texto exacto/configuracion/documentacion usar herramientas de archivos cuando sean mas adecuadas.
4. Comprobar `status` y sincronizar si la evidencia de cambios lo requiere. Si no hay indice, trabajar con lectura dirigida y preparar su inicializacion solo en el proyecto autorizado; no indexar un directorio padre amplio ni crear cobertura ficticia.
5. Relacionar hallazgos con requisitos, diseno y pruebas del cambio. La estructura estatica no demuestra todos los flujos dinamicos ni la ausencia de tests. Ejecutar verificaciones del codigo afectado y registrar limitaciones.

Guardar solo decisiones y reglas reutilizables en Engram/Git; los indices quedan locales. No instalar Gentle-AI por este skill ni prometer ahorro medido de tokens. Si un subagente no tiene acceso MCP, el padre puede pasarle contexto acotado con rutas y revision; no confundir instrucciones con permisos o herramientas.
