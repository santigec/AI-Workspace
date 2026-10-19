# codegraph-navigation-001 — Proyecto explicito y contexto reutilizado

Estado: NOT_RUN; evaluacion de comportamiento del agente pendiente.

Entrada: dos aplicaciones indexadas con una clase de igual nombre. El usuario pregunta por el flujo de la segunda y el primer resultado incluye la fuente actual relevante con referencias y un archivo recortado.

Debe usar projectPath de la segunda aplicacion, limitar archivos y reutilizar la fuente suficiente. Recuperar solo el fragmento recortado necesario. No consultar el workspace por defecto, leer todos los archivos otra vez ni asumir que el maximo de archivos fija el numero de tokens.

Registrar herramienta, argumentos, archivos usados, lecturas adicionales y razon. Una prueba del protocolo MCP no equivale a ejecutar este caso del agente.
