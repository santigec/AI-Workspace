# Resultado mug-order-intake-001

- Estado de evaluación: **PASS**.
- Alcance: logical_order_intake; no habilita promoción beta/stable.
- Workflow: mug-sublimation, alpha.
- Skill principal: product-specs 0.2.1, alpha.
- Base: commit 41e85838c67ae78738bbcd38b8f45ad82089a9d8.
- Fecha: 2026-10-14, America/Guayaquil.
- Ejecutor: Codex, lectura de workflow, catálogo y contratos; validación Python 3.12 con jsonschema 4.26.0.
- Orden operativa: fuera del repositorio, conservada localmente.
- SHA256 de order.yaml: 5ea34f44d79f5091a2645c06a3f503b8a3d7398477074eb152db174cd5037936.
- Evidencia ejecutada: [JSON de resultados](result-001.json).

## Observaciones

Los ocho controles de entrada pasan: producto, workflow, dimensiones propuestas, nombre con tilde conservado, borrador permitido, advertencia de producto no verificado, ausencia de aprobación de impresión y rechazo de producción incompleta.
validate_order devuelve DRAFT_ALLOWED, dimensiones 205 × 95 mm con dimension_source catalog y advertencia Product specifications are unverified.
Al cambiar solo mode a production, devuelve INVALID porque resolution_ppi es null. No se sustituye por 300 ni se fabrica una ficha confirmada.

## Etapas previstas

product-specs ejecutado como consulta y ficha. image-generation produciría arte nuevo; image-analysis revisaría ese resultado. sublimation-layout y resize-to-print prepararían el derivado confirmado. print-ready-qa inspeccionaría el PNG final.
image_generation, layout_generation y visual_qa: **NOT_RUN**. No se produjo archivo gráfico.

## Pendientes

Modelo y proveedor; confirmar dimensiones, área imprimible, zonas excluidas, margen, sangrado, resolución, color y espejo. Generar arte y verificar nombre, proporción, continuidad, transparencia real y QA.
No cambian los estados alpha de los skills ni unverified del producto.
