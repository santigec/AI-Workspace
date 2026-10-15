---
name: agenda-design
description: Diseña conjuntos de agenda temática A4 con portadas, reversos, datos, calendarios, actividades y cuadrícula de bajo consumo de tinta, más dos etiquetas.
---

# agenda-design

## Entrada

Recibe temática, imágenes opcionales, nombre y textos exactos si hay personalización, estilo y años. No arrastres nombres ni temática de otros pedidos.
Resuelve el año actual con la fecha del usuario/chat y el siguiente sumando uno; al 2026-10-15 corresponden **2026 y 2027**. No fijes estos años para siempre. Si se indican otros, respétalos y registra la elección.
Por defecto usa **A4 vertical de 210 × 297 mm** para las páginas. Si se pide otra orientación confirma el reparto antes de producir el conjunto.
Lee [workflow](../../../workflows/tribe/agenda-design.md), [especificaciones](../../knowledge/agenda-specs.json), [reglas visuales](../../standards/agenda-design-rules.md), [contrato de pedido](../../schemas/agenda-order.schema.json) y [resiliencia](../../policies/non-blocking-generation.md).

## Conjunto base

Entrega modelos separados, no un collage:
1. Portada frontal A4.
2. Portada posterior A4.
3. Reverso interior de portada frontal A4.
4. Reverso interior de portada posterior A4.
5. Hoja de datos importantes A4.
6. Calendario del año actual A4.
7. Calendario del siguiente año A4.
8. Hoja de actividades importantes, con líneas y columnas, A4.
9. Hoja cuadriculada A4.
10. Etiqueta principal **205 × 165 mm**.
11. Etiqueta complementaria de empaque **205 × 95 mm**.

Son nueve modelos A4 y dos etiquetas, no el número obligatorio de hojas físicas de una agenda. Repeticiones y páginas adicionales dependen del pedido.
La etiqueta de 205 × 165 mm no es A4. La de 205 × 95 mm es una etiqueta de empaque, no un diseño de taza.

## Dirección visual

Define una identidad común: paleta, tipografías, personajes/motivos, tratamiento gráfico y jerarquía. Cada pieza adapta su composición al propósito y espacio; no estires una portada para producir las otras.
Arte creativo, profesional, limpio, legible y adecuado a la temática. Conserva tipografía e identidad del original cuando se exija; para nombres personalizados respeta escritura, acentos y coherencia tipográfica. Si no hay nombre solicitado, no inventes uno: conserva motivos de la temática.
Portadas: por defecto solo temática y nombre si se solicita. No añadir «Agenda», año, eslóganes o títulos genéricos salvo petición explícita. Mantén protagonismo de personajes, emblemas y elementos originales del tema.
Etiquetas: composición propia más viva y atractiva, con contraste, color y motivos reconocibles. Adapta la energía a la referencia y al estilo solicitado (armónico, vibrante, deportivo, masculino, femenino u otro), sin deducir género por el nombre ni imponer colores estereotipados. Conserva armonía y tipografía temática; no traslades la austeridad de las hojas interiores a las etiquetas. Sin «Agenda», años o eslóganes por defecto.
Clasifica referencias de contenido, estilo o fondo. Si se adjunta una captura, no copies UI, precio ni ficha comercial. Para fidelidad exacta usa edición apropiada o declara límites.
No agregues marcas de corte, espiral, botella ni mockup al arte plano final. No inventes sangrado, tamaño de lomo o compensación de encuadernación.

## Interiores de bajo consumo

La base blanca debe sentirse diseñada y profesional a tamaño real, no vacía. Usa jerarquía editorial, secciones claramente agrupadas, módulos útiles, filetes finos y motivos temáticos visibles en cabecera, pie o márgenes. No resuelvas todas las hojas con un título, un personaje diminuto y líneas aisladas. Evalúa la composición de cada hoja por separado, además de la vista del conjunto.
Distribuye el contenido según su función: datos por grupos de identificación/contacto/emergencia, calendario con doce módulos mensuales legibles y actividades con periodo, prioridades y seguimiento. Los reversos pueden contener objetivos, recuerdos o reflexiones con ilustración proporcionada. Estos son recursos de composición, no páginas adicionales obligatorias ni campos personales que deban rellenarse inventando datos.
Evita añadir adornos solo para llenar espacio: cada bloque debe mejorar la lectura, la organización o el reconocimiento temático. Conserva áreas de escritura cómodas, blancos intencionales y contraste suficiente de líneas y textos. Un fondo blanco de bajo consumo no exige una composición mínima ni tipografía diminuta.

Datos, calendarios, actividades y cuadrícula tienen **base blanca sin fondo sólido de color**. El color temático se concentra en cabeceras, pies y acentos pequeños; el área de escritura queda despejada.
Los reversos interiores también conservan base blanca, con ilustración y motivos temáticos bien distribuidos. Las portadas exteriores pueden tener fondo temático completo.
La cuadrícula lleva siempre un motivo central de la temática como marca de agua tenue, sin tapar líneas ni escritura. Opacidad sugerida 4–8 %, ajustada según la muestra impresa. No pongas una ilustración saturada a página completa.
En hojas cuadriculadas, cabeceras y pies son gráficos y temáticos: personajes, logos/emblemas disponibles y nombre solo si se pidió. No añadir títulos informativos («Ideas y apuntes», «Ideas que toman forma»), eslóganes, campos «Tema/Fecha» ni descripciones funcionales por defecto. Mantén el carácter y tipografía del tema con acabado profesional.
Diseña la cabecera como una composición ilustrada propia: lettering o emblema temático con jerarquía, personajes integrados y adornos característicos (por ejemplo, destellos, cintas de luz y motivos musicales para K-pop). No basta un texto en negrita/cursiva de una fuente común junto a una miniatura. Usa arte generado o recursos originales adecuados para elaborar esta banda gráfica; no simules fidelidad de logotipo con una fuente genérica. El pie debe acompañar con un tratamiento temático coordinado, sin repetir información funcional. Distribuye acentos en los márgenes con intención, conserva la marca de agua central tenue y una zona de escritura amplia y blanca. Elabora según el tema, sin convertir los motivos de K-pop en requisitos de otras temáticas.
Datos: título «Datos importantes», sin subtítulos motivacionales, frases decorativas ni nombre personalizado en cabecera/pie. Campos útiles de nombre, contacto y contacto de emergencia con espacios vacíos para completar a mano. No prellenar el nombre aunque se haya solicitado para portadas o etiquetas; solo completar datos si el usuario pide explícitamente rellenar la ficha.
Actividades: columnas Fecha, Actividad, Prioridad, Estado y Notas como punto de partida, ajustables a la actividad real; filas con espacio para escribir.
Cuadrícula y líneas deben ser geométricamente regulares y finas. Usa herramientas deterministas para tablas, líneas, tipografía y maquetación cuando estén disponibles; no confíes esos detalles a una imagen generativa.

## Calendarios exactos

Calcula días, semanas, meses y años bisiestos con una biblioteca de fechas o código verificado. Para español usa nombres de meses y días correctos; semana comienza en lunes por defecto, configurable por pedido.
El título visible debe ser «Calendario» y el año correspondiente, por ejemplo «Calendario 2026»; no sustituirlo por «Mi año». Compón una cabecera atractiva y temática sin restar legibilidad a los doce meses.
No uses cifras de calendario dibujadas por el modelo de imágenes como fuente de verdad. Genera ilustraciones aparte y compón texto y fechas mediante maquetación determinista.
El [planificador](../../../scripts/build_agenda_plan.py) valida el pedido y exporta datos de calendario y un manifiesto de piezas; **no genera imágenes ni archivos de impresión**.
No inventes feriados: solicita país/región si se necesitan.

## Ejecución, QA y entrega

Si el usuario pide generar el conjunto, genera todas las piezas acordadas con la herramienta de imágenes disponible y maquetación; no lo sustituyas por un brief o un manifiesto. Si falta una herramienta, informa qué artefactos quedaron pendientes.
Muestra previsualizaciones e identifica cada archivo. Usa PNG para imágenes solicitadas y un documento con tamaño físico exacto cuando sea necesario para impresión; en documentos con texto o tablas, conserva su legibilidad.
Verifica cada dimensión física, proporción, píxeles y resolución efectiva. A 300 ppp los objetivos redondeados son A4 **2480 × 3508 px**, etiqueta 205 × 165 **2421 × 1949 px**, empaque 205 × 95 **2421 × 1122 px**. No declares 300 ppp si la herramienta produjo otra resolución.
Comprueba todos los días de los dos calendarios, texto sin errores, nombre si corresponde, continuidad visual, contraste y áreas libres para escribir. Confirma la presencia de la marca de agua central y cabeceras/pies temáticos en la cuadrícula.
Revisa páginas y etiquetas como conjunto, con inventario de entregables y pendientes, usando [checklist](../../templates/agenda-qa.md).
Guarda pedidos, imágenes y datos personales fuera de Git; design-runs queda local e ignorado. El usuario prioriza sincronizar conocimiento: guardar decisiones y correcciones en Engram del proyecto ai-workspace y versionar .engram junto con skills/reglas según AGENTS.md. No incorporar archivos pesados ni bases SQLite. La aprobación de estructura o calendario no certifica impresión: PRINT_READY requiere revisar artefactos reales, márgenes, encuadernación y parámetros de impresión del pedido.
