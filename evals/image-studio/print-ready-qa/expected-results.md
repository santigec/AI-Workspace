# Resultados esperados: print-ready-qa

Estado inicial de todos los casos: **NOT_RUN**. Requieren ejecución y evidencia según [la guía](../../../standards/evaluation-guide.md).

## print-ready-qa-001

- Comprueba archivo real y registra evidencia por criterio.
- PASS solo si todos los requisitos críticos fueron verificados.
- No modifica el arte; artifact referencia el archivo revisado.

## print-ready-qa-002

- Calcula resolución efectiva: aproximadamente 126.88 y 127 ppp.
- FAIL por resolución insuficiente aunque metadatos indiquen 300.
- Distingue reescalado de recuperación de detalle.

## print-ready-qa-003

- No afirma transparencia real por apariencia.
- Marca alfa NOT_VERIFIED y devuelve FAIL.
- Solicita el archivo original y no lo aprueba con warnings.
