---
name: drawstring-backpack-sublimation
description: Diseña arte A3 vertical para mochilas de cordón sublimadas, con franja superior corrugable, motivo central visible y banda inferior para logotipos solicitados.
---

# drawstring-backpack-sublimation

## Formato y alcance

Genera una sola imagen **plana A3 vertical de 297 × 420 mm** para el frente de una mochila de cordón. No entrega un mockup, una mochila en perspectiva ni piezas separadas. A 300 ppp el objetivo redondeado es **3508 × 4961 px**; si la herramienta genera menos detalle, informa el tamaño fuente y no presentes el remuestreo como detalle nativo.

Usa `product.id: drawstring_backpack_a3`. Las medidas describen el lienzo solicitado por el usuario, no una plantilla universal ni una ficha de proveedor verificada. Sangrado, margen seguro, costuras, tolerancias y espejo siguen pendientes hasta recibir la plantilla física.

## Zonas de composición

- **Franja corrugable superior:** ocupa el 25% del alto, **y = 0–105 mm**. Debe quedar completamente pintada con la continuidad del fondo, textura o borde, pero sin rostros, texto, logotipos, emblemas ni detalles indispensables; el cordón comprime esta zona y reduce su visibilidad.
- **Zona principal visible:** comienza debajo de y = 105 mm. Centra el motivo temático principal en el ancho y distribúyelo dentro de la zona visible sin deformarlo. Mantén caras, manos, texto y otros elementos esenciales fuera de la franja corrugable y lejos de los bordes físicos.
- **Banda inferior de marca:** usa como propuesta **y = 350–420 mm** para logotipos, nombre o texto que el usuario proporcione. No inventes marcas ni frases. Si no se entrega un logotipo, conserva allí fondo temático y ornamentos secundarios de baja complejidad.
- El motivo principal puede ocupar parte de la banda inferior solo cuando no existan logotipos solicitados y la composición siga siendo legible; nunca desplaces contenido crítico hacia la franja superior para hacer espacio.

## Fondo y borde

Pinta todo el A3, incluida la franja superior. Extiende el fondo de forma coherente y evita un póster pequeño flotando sobre un lienzo vacío. Puede usarse un borde temático completo, pero debe ser más discreto en la zona corrugable y no invadir rostros, título o logos.

Respeta la apariencia de las referencias como contenido, estilo o fondo. Conserva paleta, personajes, lettering y emblemas requeridos. Elimina marcos de captura, precios, UI, QR y elementos comerciales ajenos al arte. No heredes nombres de otros pedidos.

## Ejecución y entrega

Usa image-generation para arte nuevo o image-editing cuando se deba preservar un original accesible. Si el usuario pide diseño, genera y muestra el archivo real; un brief no completa el pedido.

Comprueba orientación A3, dimensiones, franja superior de 105 mm, ubicación del motivo, banda inferior, legibilidad y fondo completo. No añadas guías ni cotas al arte visible salvo solicitud. No apliques espejo automáticamente.

Entrega previsualización, archivo, dimensiones, tamaño fuente cuando haya remuestreo y estado. Usa **DRAFT** mientras falten plantilla física, sangrado, margen, costuras o QA de impresión; `PRINT_READY` requiere verificación real del archivo y del producto.
