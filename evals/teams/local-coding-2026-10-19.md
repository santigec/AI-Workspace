# Conexion opcional LM Studio / Qwen — 2026-10-19

Pedido: usar Qwen solo como apoyo de codificacion en este PC; Codex para coordinacion/analisis/diseno/revision/pruebas y para toda la codificacion en PCs sin IA local.

## Evidencia ejecutada

- `lms server start --port 1234 --bind 127.0.0.1`: iniciado. `Get-NetTCPConnection -LocalPort 1234 -State Listen`:127.0.0.1. La captura inicial mostraba servidor detenido y LAN activada; se arranco explicitamente en loopback, no se habilito CORS.
- GET /api/v1/models: Qwen2.5 Coder7B Instruct Q4_K_M, instanceid qwen2.5-coder-7b-instruct, contexto8192, trained_for_tool_use=false. Otros modelos descargados no seleccionados.
- `python scripts/local_coder.py probe`: READY.
- `propose` con tarea sintetica clamp: PROPOSAL_REQUIRES_REVIEW, finish_reason stop,140tokens entrada+136salida=276 observados. No representan ahorro comparativo.
- Funcion revisada manualmente antes de ejecutarla desde Codex: casos valor interior, inferior/superior fuera, ambos limites, rango degenerado, negativos, flotante y limites invertidos:9PASS. El adaptador no ejecuto ni aplico la propuesta.
- `python -m unittest discover -s tests -p test_local_coder.py -v`:11PASS. Servidor loopback simulado: ausente/deshabilitado sin red, cargado/no cargado, modelo exacto, propuesta sin cambios, contexto sensible/fuera/budget, timeout, respuesta invalida/truncada, URL no local y redireccion. Ejecucion con permisos locales de sockets. Primer intento en sandbox no pudo escribir temporales predeterminados; fixtures movidos al workspace y ejecucion posterior correcta.
- Validacion OpenSpec estricta:4items PASS antes de archivar.
- Tras incorporar el conocimiento pendiente solicitado por el usuario: validacion de registro43skills PASS;71pruebas Python PASS en copia del conjunto publicable (sin runtimes/salidas locales) y6pruebas OpenSpec PASS. Los17skills recuperados siguen experimental y sin evaluacion de comportamiento; esos resultados tecnicos no los promueven.

## Limites

No se modifico model_provider de Codex ni se configuro un subagente nativo Qwen. Regla de enrutamiento en AGENTS, adaptador HTTP explicito y configuracion local ignorada; no daemon ni sincronizacion de modelos. No se probaron todavia SITOP/Tribe Sport/SPI, calidad general de Qwen ni otro equipo fisico. La ausencia de IA se prueba con fixtures; no equivale a instalacion validada en el segundo PC. JIT del servidor sigue siendo una preferencia de LM Studio; ver guia sobre la ventana entre comprobacion de carga y generacion. No se alteraron diagramas de productos: este adaptador no cambia su codigo/arquitectura; diseno textual proporcional en OpenSpec.
