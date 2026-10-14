---
name: sql-review
description: Revisa consultas SQL para detectar errores de lógica, rendimiento y efectos sobre datos.
---

# sql-review

Identifica motor y versión, esquema, volúmenes y objetivo de la consulta.
Revisa joins, cardinalidad, NULL, filtros, agregaciones y límites transaccionales.
Sustenta observaciones de rendimiento con plan de ejecución o márcalas como hipótesis.
Propón correcciones con ejemplos concretos y preserva la semántica solicitada.
No ejecutes escrituras como parte de una revisión. Entrega hallazgos priorizados y SQL propuesto cuando aplique.
