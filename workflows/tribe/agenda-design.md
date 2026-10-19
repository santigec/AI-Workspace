# Diseño de agenda

## Entrada y planificación

Usa agenda-design con tema, referencias opcionales, textos exactos si se personaliza y dos años consecutivos. Si no hay años, resuelve actual/siguiente con la fecha del usuario antes de construir la orden.
Consulta [especificaciones](../../tribe/knowledge/agenda-specs.json) y [schema](../../tribe/schemas/agenda-order.schema.json). A4 vertical por defecto; dos etiquetas con tamaños propios.
product-specs recopila impresión, encuadernación y medidas pendientes. El plan base son nueve modelos A4 y dos etiquetas; confirma copias o páginas adicionales.

## Dirección y arte

image-analysis inspecciona las referencias si existen. professional-writing revisa nombres, instrucciones y campos.
image-generation crea ilustraciones, lettering, marcos, iconos, motivos y bandas decorativas; image-editing adapta originales cuando corresponde. Mantén tipografía e identidad temática. Antes de producir páginas, define paleta, lettering, motivos, marco, ilustración y componentes reutilizables según [interiores vibrantes](../../tribe/skills/agenda-design/references/vibrant-interiors.md). No pidas al modelo de imágenes que invente la matriz de fechas.

## Maquetación

Usa herramientas disponibles para componer texto, tablas, líneas y cuadrícula regulares, y datos de calendario calculados.
El planificador scripts/build_agenda_plan.py exporta un plan y datos; no sustituye arte final.
Portadas exteriores pueden usar fondo temático. Reversos interiores, datos, calendarios, actividades y cuadrícula conservan base mayormente blanca, pero cada pieza debe tener cabecera expresiva, estructura funcional tematizada y marco, pie o acento visible. Usa personajes o emblemas como ilustración integrada o marca de agua, no como miniaturas sueltas. Cuadrícula con marca de agua central, cabecera y pie temáticos.
Cada etiqueta se recompone a su propio formato sin estirar A4.

## QA y entrega

resize-to-print comprueba formatos y resolución sin deformar. print-ready-qa revisa archivos reales con [checklist](../../tribe/templates/agenda-qa.md), primero cada página al 100 % y luego la vista conjunta. Una página genérica, vacía o decorada solo en la cabecera falla aunque sus medidas sean correctas.
El calendario exige revisión de fechas, no solo visual. Entrega un archivo por modelo, previsualización e inventario; PDF con medidas reales si se genera, PNG cuando sea solicitado.
No declarar PRINT_READY con fechas o páginas pendientes. Un plan de piezas no es una agenda generada.
