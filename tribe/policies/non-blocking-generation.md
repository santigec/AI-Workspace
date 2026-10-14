# Generación no bloqueante

Avanzar en la parte posible del pedido, preservando restricciones hard. No permite ignorar restricciones, sustituir una herramienta fallida con éxito ficticio ni eludir límites de herramientas.

## Prioridad

1. Conservar nombre, temática, identidad y elementos esenciales.
2. Adaptar solo elementos soft autorizados: distribución, escala proporcional, adornos secundarios y fondo cuando no sea hard.
3. Documentar adaptaciones y limitaciones reales.

## Datos pendientes

Con mode draft y allow_draft_on_missing_specs true, generar un borrador a medidas solicitadas o propuestas, declarando fuente y pendientes. No ejecutar sublimation-layout con especificaciones incompletas como si su contrato de producción estuviera satisfecho.
Usar image-generation para arte nuevo o image-analysis e image-editing para original accesible. Sin herramientas, entregar brief y BLOCKED; no anunciar un archivo generado.
Con mode production, no convertir silenciosamente a draft. Puede ofrecerse un borrador separado para decisión. La producción sigue bloqueada hasta confirmar ficha y QA.

## Estados de ejecución

- DRAFT: archivo de exploración producido; production_ready false.
- READY_FOR_QA: entrada completa y archivo final producido, pendiente de QA.
- PRINT_READY: QA real PASS o PASS WITH WARNINGS con todos los requisitos críticos verificados.
- BLOCKED: contradicción hard, original crítico ausente o imposibilidad de producir artefacto útil.

El validador solo devuelve DRAFT_ALLOWED, INPUT_READY, INVALID o BLOCKED_PRODUCTION. INPUT_READY no implica archivo ni aprobación de impresión. Ninguna ejecución se inventa para satisfacer no bloquear.
