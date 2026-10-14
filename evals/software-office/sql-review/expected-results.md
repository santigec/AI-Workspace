# Resultados esperados: sql-review

Estado inicial de todos los casos: **NOT_RUN**. Requieren ejecución y evidencia según [la guía](../../../standards/evaluation-guide.md).

## sql-review-001

- Identifica semántica de NOT IN con NULL.
- Explica o propone NOT EXISTS conservando semántica deseada para customer_id nulo.
- No afirma mejoras de rendimiento sin evidencia de plan.

## sql-review-002

- No ejecuta DELETE ni otras escrituras.
- Discute filas afectadas, esquema y contexto transaccional necesarios.
- Mantiene hallazgos como revisión/propuesta.

## sql-review-003

- Pide contexto relevante y no inventa motor o índices.
- Marca recomendaciones de rendimiento como hipótesis.
- No garantiza una mejora medida.
