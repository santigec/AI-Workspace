---
name: mug-box-design
description: Diseña arte plano y continuo para cajas de taza de 150 × 200 mm con tipografía temática, borde decorado, motivos inferiores laterales y centro inferior libre.
---

# mug-box-design

## Entrada y formato

Recibe temática, referencias opcionales, textos exactos, nombre solo si se solicita y dirección visual. Si existe arte de la taza, úsalo como referencia de identidad para coordinar caja y taza sin estirar su composición.
El lienzo es vertical de **150 mm de ancho × 200 mm de alto (15 × 20 cm)**, plano y continuo. Es un arte de empaque, distinto de la banda de taza de 205 × 95 mm. No entregar un mockup, una caja en perspectiva, caras separadas ni un troquel inventado.
Consulta [reglas de composición](../../standards/mug-box-design-rules.md), [workflow](../../../workflows/tribe/mug-box-design.md) y [QA](../../templates/mug-box-qa.md).

## Composición obligatoria

- Mantén un fondo temático continuo en todo el lienzo, también bajo el centro inferior libre. Continuo significa una composición sin cortes visuales, no una repetición de mosaico ni una unión lateral perfecta salvo solicitud expresa.
- Coloca artes reconocibles de la temática en las zonas **inferior izquierda e inferior derecha**, con escala y contraste equilibrados.
- Reserva el **centro inferior sin textos, personajes, emblemas ni ornamentos protagonistas**; permite solamente el fondo de baja complejidad. Evita que los motivos laterales o el borde invadan esta reserva.
- Sitúa el tema, lettering o emblema principal en el **centro superior**. La referencia de altura es **120 mm desde la base**, equivalente a **80 mm desde arriba**: es un anclaje de composición, no el tamaño del título ni una franja inferior de 120 mm totalmente vacía.
- Decora **todo el perímetro** con un borde coherente con el tema, manteniendo el centro inferior despejado. El borde inferior puede ser discreto para respetar la reserva.
- Integra tipografía, colores, emblemas y detalles propios del tema. Usa colores vibrantes con jerarquía profesional, limpieza y legibilidad; no llenes cada espacio de adornos.

No se han definido las medidas exactas de la reserva central, grosor del borde, cortes, pliegues, pestañas ni sangrado. Para un borrador elige una reserva visual clara y registra su extensión; para producción ajústala a la plantilla física confirmada. No inventes esos parámetros ni presentes esta composición como un troquel validado.

## Identidad y referencias

Conserva la tipografía o lettering de la temática cuando esté disponible; si se exige fidelidad exacta, usa el recurso original accesible o declara la limitación. No afirmes que una fuente genérica reproduce un logo. Personaliza nombres respetando escritura y acentos solo cuando se soliciten; no heredes nombres de otros pedidos ni agregues frases genéricas.
Adapta borde, energía y motivos al estilo pedido, incluido femenino o masculino cuando se indique. No deduzcas género por el nombre ni impongas colores estereotipados. La paleta pertenece a la temática del pedido; no a la marca de la tienda por defecto.
Clasifica las imágenes como original, contenido, estilo o fondo. Una captura comercial no autoriza copiar UI, precios, QR, teléfonos ni elementos ajenos al arte.

## Ejecución y entrega

Cuando se pida generar, usa image-generation o image-editing según el caso y muestra el arte resultante; una ficha o un prompt no sustituyen la imagen. Inspecciona archivo y composición reales con print-ready-qa. Si falta una herramienta o referencia indispensable, indica lo pendiente sin fingir generación.
Mantén la proporción **3:4** sin deformar ilustraciones. A 300 ppp el objetivo redondeado es **1772 × 2362 px**; el tamaño físico de maquetación sigue siendo 150 × 200 mm. Comprueba dimensiones y resolución efectiva, sin declarar 300 ppp por simple reescalado o metadatos. Si hace falta tamaño físico exacto, compón un documento de 150 × 200 mm sin recortar contenido crítico.
Entrega previsualización, archivo, dimensiones, extensión de la reserva y limitaciones. No añadas cotas, guías, líneas de pliegue ni marcas de corte al arte visible salvo solicitud. La condición PRINT_READY requiere archivo final revisado y parámetros de producción confirmados; mientras falte plantilla o zona libre exacta, identifica el resultado como borrador.
Guarda diseños y pedidos reales fuera de Git. Versiona únicamente reglas, skills, plantillas y conocimiento conforme a AGENTS.md.
