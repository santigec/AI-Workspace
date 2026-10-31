---
name: bolsitos-colorear-a3
description: Crea plantillas A3 verticales para mochilas de cordón infantiles, transformando una referencia en line art negro limpio sobre blanco con espacios cerrados y amplios para colorear.
---

# bolsitos-colorear-a3

## Formato y alcance

Genera una sola imagen **plana A3 vertical de 297 × 420 mm** para una mochila de cordón destinada a colorear. No entrega mockup, perspectiva ni piezas separadas. A 300 ppp el objetivo redondeado es **3508 × 4961 px**; si la fuente es menor, informa sus dimensiones y no presentes el remuestreo como detalle nativo.

Usa `product.id: drawstring_backpack_coloring_a3`. Las medidas son una propuesta del usuario, no una plantilla universal verificada. Mantén el estado **DRAFT** hasta confirmar plantilla, sangrado, márgenes, costuras, espejo y prueba física.

## Lenguaje gráfico para colorear

- Produce **line art negro puro sobre fondo blanco opaco**. El blanco debe ocupar el interior de las figuras y los espacios que los niños pintarán.
- Usa contornos nítidos, continuos y preferentemente cerrados, con grosor suficiente para impresión. Puede variar el peso de línea para jerarquía, sin perder limpieza.
- Conserva personajes, pose, vestuario, objetos, temática y composición reconocibles de la referencia, reinterpretándolos como dibujo profesional para colorear.
- Mantén detalles significativos y regiones amplias para rellenar. Simplifica texturas, brillos y adornos diminutos que generarían ruido o áreas imposibles de colorear.
- Evita color, grises, sombras, degradados, semitonos, tramados, texturas fotográficas, manchas, fondos negros, grandes rellenos sólidos y sombreado cruzado. Pupilas pequeñas y acentos mínimos pueden ser negros.
- El resultado no es una fotografía desaturada ni un filtro de bordes: debe ser una ilustración redibujada con anatomía, expresiones y contornos coherentes.

## Zonas de composición

- **Franja corrugable superior:** ocupa el 25% del alto, **y = 0–105 mm**. Debe permanecer blanca o llevar solo ornamentos de contorno muy dispersos; no coloques rostros, texto, logotipos ni detalles indispensables.
- **Zona principal visible:** comienza debajo de y = 105 mm. Centra el motivo principal y conserva rostros, manos, elementos esenciales y contornos completos lejos de la franja corrugable y de los bordes físicos.
- **Banda inferior:** usa como propuesta **y = 350–420 mm** para título, nombre o logotipo que el usuario entregue. El lettering debe ser hueco o delineado para poder colorearse. Si no hay texto, usa ornamentos simples de contorno.
- Puede existir un borde temático delineado, pero debe ser discreto y todavía más liviano en el 25% superior.

## Tratamiento de referencias

Usa image-analysis cuando haya una referencia para separar contenido, estilo y fondo. Conserva los rasgos artísticos relevantes, pero elimina marcos de captura, UI, precios, QR y elementos comerciales ajenos. No heredes nombres de otros pedidos.

Usa image-generation para redibujar el arte o image-editing cuando se deba preservar una composición accesible. Si el usuario pide el diseño, genera y muestra el archivo real; un brief no completa el pedido.

## Revisión y entrega

Comprueba orientación A3, dimensiones, franja superior de 105 mm, motivo debajo de esa zona, banda inferior, fondo blanco, ausencia de color/gris/sombras, contornos cerrados, legibilidad y espacios coloreables. No añadas guías ni cotas visibles. No apliques espejo automáticamente.

Entrega previsualización, archivo, dimensiones, tamaño fuente si hubo remuestreo y estado. `PRINT_READY` requiere verificación real del producto y del archivo; de lo contrario entrega **DRAFT**.
