# print-ready-qa-002: Resolución insuficiente

## User request

Este archivo dice 300 DPI: confirma que sirve para 205 × 95 mm.

## Entradas de prueba

Proveer PNG de 1024 × 475 px; ficha exige 300 ppp y tamaño de 205 × 95 mm.

## Expected behavior

- Calcula resolución efectiva: aproximadamente 126.88 y 127 ppp.
- FAIL por resolución insuficiente aunque metadatos indiquen 300.
- Distingue reescalado de recuperación de detalle.

## Ejecución

NOT_RUN. Registrar resultado usando [la plantilla](../../result-template.md).
