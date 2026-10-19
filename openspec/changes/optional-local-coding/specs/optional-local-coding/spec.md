## ADDED Requirements

### Requirement: LC-01 Activacion local explicita y alcance
El trabajador SHALL solicitar propuestas de codigo solo cuando exista configuracion local habilitada y el modelo elegido ya este cargado. Codex MUST conservar las demas funciones y revisar la propuesta antes de aplicarla.

#### Scenario: Equipo habilitado
- **WHEN** el equipo tiene configuracion habilitada y Qwen cargado en LM Studio
- **THEN** el trabajador envia un pedido acotado por HTTP loopback y devuelve una propuesta identificada por modelo, sin aplicarla ni ejecutarla.

#### Scenario: Equipo sin IA local
- **WHEN** falta configuracion, servidor o modelo cargado, o la generacion falla
- **THEN** devuelve FALLBACK_TO_CALLER y Codex continua; no descarga modelos, no cambia proveedor y no llama a otra API.

### Requirement: LC-02 Contexto y limites
El trabajador MUST aceptar solo contexto textual explicito dentro del proyecto, rechazar secretos conocidos y limitar entrada, salida y esperas. Las respuestas SHALL tratarse como propuestas sin autoridad para dar instrucciones al coordinador.

#### Scenario: Contexto invalido
- **WHEN** un archivo sale del proyecto, es sensible o supera el presupuesto
- **THEN** se rechaza antes de enviar la generacion y no modifica archivos del proyecto.

#### Scenario: API no local o respuesta invalida
- **WHEN** la configuracion intenta salir de loopback, hay redireccion o la respuesta es invalida/incompleta
- **THEN** el trabajador no sigue redirecciones y retorna FALLBACK_TO_CALLER con motivo, sin ejecutar contenido recibido.
