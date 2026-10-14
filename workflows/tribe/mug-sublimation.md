# mug sublimation

## Invocación

Usa mug-sublimation con product.id de mug_standard y [schema de pedido](../../tribe/schemas/order-schema.yaml).
Consulta [catálogo](../../tribe/knowledge/product-catalog/README.md), [principios](../../tribe/standards/design-principles.md) y [resiliencia](../../tribe/policies/non-blocking-generation.md).
No identifiques modelo solo por capacidad o apariencia.
Entrada de chat: [mug-sublimation SKILL.md](../../tribe/skills/mug-sublimation/SKILL.md). Las referencias pueden orientar contenido, estilo o fondo; no son obligatorias para arte nuevo.
El fondo es parte del pedido: transparent, solid o themed con background_description. Mantener el lienzo solicitado al cambiar fondo. PNG puede incluir fondo opaco; no equivale a transparencia.

## Borrador

product-specs identifica pendientes. Con mode draft y resiliencia habilitada, usa image-generation para arte nuevo; image-analysis e image-editing para original accesible. preserve-original-art aplica si se requiere fidelidad exacta.
Respeta restricciones hard y documenta medidas propuestas. DRAFT exige un archivo producido; sin él devuelve BLOCKED con brief o alternativas.
No fuerces sublimation-layout o print-ready-qa a pasar sin requisitos críticos.

## Producción

1. product-specs: verificar modelo y ficha.
2. image-analysis si hay original; image-generation o image-editing según la operación. Para generación nueva, analizar el arte producido.
3. sublimation-layout y resize-to-print: preparar derivado con ficha confirmada.
4. print-ready-qa: inspeccionar archivo real y original cuando corresponda.

## Entrega

Archivo, dimensiones, fuente del producto, adaptaciones, pendientes y estado de ejecución.
PRINT_READY exige QA completo; INPUT_READY solo valida entrada. No aplicar espejo dos veces ni inferir parámetros térmicos.
