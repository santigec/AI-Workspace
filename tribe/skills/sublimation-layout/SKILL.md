---
name: sublimation-layout
description: Prepara una composición para sublimación usando el área imprimible del producto confirmado.
---

# sublimation-layout

## Input Contract

Required: product_type y modelo, artwork accesible, product_spec confirmado con dimensiones y unidades, área imprimible, resolución, fondo y política de espejo.
Optional: supplier, bleed, safe_margin, crop_permission.
Consulta [especificaciones](../../knowledge/print-specs.md) y [ficha](../../templates/product-spec.md). Una medida explícita puede definir un lienzo de prueba, pero no confirma por sí sola el área imprimible del producto.

## Procedimiento

Usa image-analysis y product-specs como evidencia previa.
Ajusta al área confirmada conservando proporción. Ante incompatibilidad, usa contener o ampliar lienzo; explica espacio libre. Recortar contenido crítico requiere una decisión explícita del usuario.
Respeta márgenes, uniones y zonas excluidas. No asumas un sangrado universal.
Confirma quién aplica espejo: proveedor, RIP o usuario. Registra not_required, applied_here o delegated; unknown bloquea producción.
Si faltan herramientas para producir el archivo, entrega diagnóstico y FAIL con reason: unsupported_operation; no llames arte final a una descripción.
Conserva el original. Verifica dimensiones reales del derivado; usa resize-to-print si hace falta.

## Output Contract

status, evidence, warnings, missing_inputs, artifact.
final_dimensions: ancho_mm, alto_mm, ancho_px, alto_px, ppp.
aspect_ratio, layout_decision, crop_decision, mirror_status, product_spec_source.
next_skill: print-ready-qa cuando exista derivado; product-specs si faltan especificaciones.

## Criterios

PASS: archivo producido con medidas, área y márgenes confirmados; proporción preservada y contenido crítico intacto.
PASS WITH WARNINGS: requisitos críticos cumplidos con advertencias no críticas.
FAIL: producto ambiguo, medidas/área/espejo críticos pendientes, operación que destruye contenido requerido o archivo no producido.
PASS de layout requiere QA posterior para declarar arte listo para imprimir. No valida parámetros térmicos.

Casos: [evaluaciones](../../../evals/tribe/sublimation-layout/expected-results.md).
Convención: [contratos](../../../standards/skill-contract.md).
