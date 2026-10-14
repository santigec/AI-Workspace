---
name: image-analysis
description: Analiza imágenes de referencia para describir composición, texto, fondo y restricciones antes de editar o preparar arte.
---

# image-analysis

## Input Contract

Required: artwork (archivo o referencia accesible), requested_operation.
Optional: fidelity_constraints, product_spec, target_dimensions con unidades.
Si no hay imagen accesible, devuelve FAIL con reason: missing_input; no inventes su contenido.

## Procedimiento

Inspecciona composición, objetos, colores, texto legible, logos y fondo. Distingue observaciones de inferencias.
Registra formato y dimensiones en píxeles solo si se verifican en el archivo.
Una vista previa no prueba canal alfa, DPI ni dimensiones físicas.
Identifica elementos que deben conservarse y ambigüedades que afectan la operación.
Si el texto es ilegible, transcríbelo como desconocido en lugar de completarlo.

## Output Contract

status, evidence, warnings, missing_inputs, artifact (null: este skill no modifica imágenes).
image_properties: formato, ancho_px, alto_px, alpha_verified; usa null para datos no verificados.
content_summary, readable_text, fidelity_constraints, requested_changes.
next_skill: product-specs para un producto de impresión; image-editing para edición; transparent-png para extracción de fondo; resize-to-print para tamaño. Elige según intención; no inicia otra etapa automáticamente.

## Criterios

PASS: imagen inspeccionada y restricciones críticas de análisis definidas.
PASS WITH WARNINGS: diagnóstico útil con incertidumbre no crítica, por ejemplo metadatos no disponibles en una vista previa.
FAIL: imagen inaccesible o contenido crítico imposible de inspeccionar para la operación.
El estado del análisis no certifica que el arte esté listo para impresión.

Casos: [evaluaciones de Image Studio](../../../evals/image-studio/image-analysis/expected-results.md).
Convención: [contratos](../../../standards/skill-contract.md).
