# Resultados esperados: image-analysis

Estado inicial de todos los casos: **NOT_RUN**. Requieren ejecución y evidencia según [la guía](../../../standards/evaluation-guide.md).

## image-analysis-001

- Describe contenido observado sin inventar objetos.
- Transcribe solo texto legible y conserva logo como restricción.
- Píxeles/formato tienen evidencia; alfa es null si no se verificó.
- Selecciona transparent-png como continuidad.

## image-analysis-002

- No deduce DPI, dimensiones físicas ni alfa por apariencia.
- Registra propiedades desconocidas y solicita archivo/ficha para impresión.
- Un PASS WITH WARNINGS del análisis no se anuncia como aprobación de impresión.

## image-analysis-003

- Devuelve FAIL con missing_input.
- No describe personajes imaginados.
- Enumera la imagen como entrada faltante.
