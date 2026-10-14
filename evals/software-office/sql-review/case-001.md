# sql-review-001: NULL en antijoin

## User request

Revisa SELECT * FROM orders WHERE customer_id NOT IN (SELECT id FROM blocked_customers); el subquery puede devolver NULL.

## Entradas de prueba

Motor PostgreSQL; columnas y NULL confirmados, revisión sin ejecutar.

## Expected behavior

- Identifica semántica de NOT IN con NULL.
- Explica o propone NOT EXISTS conservando semántica deseada para customer_id nulo.
- No afirma mejoras de rendimiento sin evidencia de plan.

## Ejecución

NOT_RUN. Registrar resultado usando [la plantilla](../../result-template.md).
