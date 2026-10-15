---
name: tumbler-750ml-sublimation
description: Genera o adapta arte plano y continuo para tomatodo de 750 ml con lienzo de 232 mm de ancho × 182 mm de alto.
---

# tumbler-750ml-sublimation

## Entrada específica

Esta entrada selecciona exclusivamente product.id **tumbler_750ml** y lienzo **232 mm de ancho × 182 mm de alto**, confirmado por el usuario el 2026-10-15.
Modela la orden con workflow **tumbler-sublimation**, el workflow común de tomatodos, y requested_dimensions width_mm 232, height_mm 182. El nombre de este skill distingue la entrada de 750 ml; no cambia el identificador del workflow compartido.
Si el pedido indica otra capacidad, usa su variante en lugar de imponer 750 ml.
Recibe temática, nombre/texto si se solicita, fondo e imágenes de referencia opcionales; no heredes nombres de otros trabajos.

## Reglas de diseño

Aplica [las reglas comunes](../tumbler-sublimation/SKILL.md) y [el workflow](../../../workflows/tribe/tumbler-sublimation.md) con la variante 750 ml.
El arte es **plano, continuo y horizontal**, para impresión y posterior sublimación; no un mockup.
La proporción es 232:182, aproximadamente **1.275:1**. Frente al tomatodo 500 ml (232 × 125 mm), el ancho se mantiene y aumenta la altura disponible.
Recompón personajes, tipografía y entorno para utilizar esa altura y todo el ancho sin estirar ni deformar. No reutilices 125 ni 142 mm de alto ni amplíes verticalmente todo el dibujo como si fuera una escala proporcional.
Mantén nombres y elementos esenciales fuera de uniones y cortes según la plantilla; extiende el entorno con continuidad. No inventes solapes, márgenes ni compensación cónica.
Blanco, transparente o temático son opciones del pedido y no cambian 232 × 182 mm. Las referencias pueden guiar contenido, estilo o fondo. Conserva el original cuando se solicite y elimina elementos comerciales de capturas.

## Salida y verificación

Genera y muestra la imagen cuando se solicite diseño. Entrega PNG descargable y, si hace falta para fijar tamaño físico, documento de 232 × 182 mm con colocación proporcional.
Comprueba nombre, proporción, continuidad, fondo y píxeles reales. Si se exigen 300 ppp, el objetivo redondeado es **2740 × 2150 px**; no prometas esa resolución si la herramienta entrega otra.
Para producción completa la ficha mediante product-specs y aplica sublimation-layout, resize-to-print y print-ready-qa, como indica el workflow.
La medida confirmada define el lienzo del usuario; no valida modelo/proveedor ni espejo, color o parámetros térmicos. No declares PRINT_READY sin archivo final y QA completo.
