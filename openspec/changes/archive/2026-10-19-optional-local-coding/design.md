# Diseno

Un adaptador Python de biblioteca estandar hace GET /api/v1/models para comprobar loaded_instances y POST /v1/chat/completions para propuestas. Configuracion .tools/local-ai.json local ignorada; ausente significa deshabilitado. URL restringida a HTTP 127.0.0.1, sin proxies ni redirecciones; modelo identificado explicitamente, sin seleccion automatica de otro modelo. Qwen cargado en este PC tiene 8192 tokens de contexto y no esta entrenado para herramientas: mensajes de texto, entrada maxima 12000 caracteres y salida maxima 1024 tokens. Estos limites no garantizan encaje para todo idioma; error de contexto deriva a Codex.

No es un cambio de model_provider ni un subagente nativo Qwen. El rol de codificacion de Codex puede invocar este adaptador y revisar su salida. Analisis/diseno/QA/UML/Git/Engram siguen en Codex. Sin autoaplicacion, ejecucion de propuestas, instalacion global o secretos versionados. Configuracion no sincronizada; politica y pruebas si.

No se modifica UML de aplicaciones: no se ha conectado un producto ni cambiado su arquitectura. Para este adaptador pequeno el contrato y escenarios anteriores describen completamente la interaccion; no precisa diagrama nuevo. Validacion: servidor simulado para errores/limites y prueba real sintetica de Qwen con codigo revisado y pruebas ejecutadas por Codex.
