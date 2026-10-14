---
name: print-ready-qa
description: Valida arte antes de impresión contra las especificaciones confirmadas del producto.
---

# print-ready-qa

## Input Contract

Required: final_artwork accesible y product_spec con requisitos críticos confirmados.
Optional: original_artwork para fidelidad, layout_report, supplier_requirements.
Si se exige conservar el original, original_artwork pasa a ser requerido.
Usa [informe QA](../../templates/print-qa-report.md). Revisa el archivo real, no solamente una vista previa.

## Procedimiento

Verifica dimensiones físicas y píxeles, resolución efectiva, proporción, recorte, fondo o alfa real, texto, logos, márgenes, sangrado, formato y color.
Resolución efectiva: ancho_px / (ancho_mm / 25.4) y alto_px / (alto_mm / 25.4). Contrasta ambas con lo requerido; cambiar el metadato DPI no añade detalle.
Evalúa dimensiones de píxeles respecto al redondeo esperado; usa tolerancias del proveedor y no inventes una tolerancia de producción.
No infieras transparencia por un tablero pintado. Inspecciona canal alfa y bordes si la herramienta lo permite.
Compara con el original cuando corresponda. Registra por comprobación expected, observed, evidence y verdict: PASS, FAIL o NOT_VERIFIED.
Revisa el estado de espejo contra la ficha. Si no puedes verificar un requisito crítico, márcalo NOT_VERIFIED.
No modifiques el archivo como parte de QA.

## Output Contract

status, evidence, warnings, missing_inputs, artifact (archivo revisado; no un nuevo derivado).
checks, corrections, critical_pending.
next_skill: null cuando apruebe; resize-to-print para tamaño/resolución; transparent-png para fondo; sublimation-layout para márgenes o composición; product-specs para requisitos ausentes. Indica la corrección prioritaria sin ejecutarla automáticamente.

## Criterios

PASS: todas las comprobaciones críticas cumplidas y verificadas.
PASS WITH WARNINGS: requisitos críticos cumplidos y solo advertencias no críticas.
FAIL: cualquier incumplimiento crítico o comprobación crítica NOT_VERIFIED; informa reason y evidencia.
No declares PASS sin archivo final o sin especificaciones críticas.

Casos: [evaluaciones](../../../evals/image-studio/print-ready-qa/expected-results.md).
Convención: [contratos](../../../standards/skill-contract.md).
