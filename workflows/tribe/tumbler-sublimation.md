# tumbler sublimation

## Invocación

Usa tumbler-sublimation con product.id de tumbler_500ml, tumbler_600ml o tumbler_750ml y [schema de pedido](../../tribe/schemas/order-schema.yaml).
Consulta [catálogo](../../tribe/knowledge/product-catalog/README.md), [principios](../../tribe/standards/design-principles.md) y [resiliencia](../../tribe/policies/non-blocking-generation.md).
No identifiques modelo solo por capacidad o apariencia.
Entrada desde chat: [tumbler-sublimation SKILL.md](../../tribe/skills/tumbler-sublimation/SKILL.md).
Para 500 ml usa tumbler_500ml y **232 mm de ancho × 125 mm de alto**, tamaño de diseño confirmado por el usuario el 2026-10-15.
Para 600 ml usa tumbler_600ml y **232 × 142 mm**, confirmado por el usuario el 2026-10-15. Entrada específica: [tumbler-600ml-sublimation](../../tribe/skills/tumbler-600ml-sublimation/SKILL.md).
Para 750 ml usa tumbler_750ml y **232 × 182 mm**, confirmado por el usuario el 2026-10-15. Entrada específica: [tumbler-750ml-sublimation](../../tribe/skills/tumbler-750ml-sublimation/SKILL.md). Aprovecha la mayor altura mediante recomposición, sin estirar las variantes de 500 o 600 ml.
La imagen es plana y continua para impresión y posterior sublimación. Adapta el reparto gráfico al lienzo de la capacidad elegida, sin estirar el formato de taza ni el de otra variante.
Fondo y referencias se toman del pedido; blanco, transparente o temático no cambian dimensiones. Evita grandes vacíos laterales salvo que el diseño los requiera o el usuario pida encaje exacto del original.
Modelo, unión, márgenes, espejo y posibles compensaciones cónicas requieren su especificación; no se infieren de la capacidad.

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
