---
name: agenda-design
description: Diseña agendas, planners, calendarios e interiores A4 temáticos, vibrantes, funcionales y verificables.
---

## Activation Contract

Usa este skill para generar o adaptar agendas, planners, calendarios, hojas de datos, actividades, cuadrículas y etiquetas. Recibe temática, referencias, nombre o textos exactos, años y parámetros de impresión. Si no se indican años, usa el actual y el siguiente según la fecha del chat.

## Hard Rules

- Entrega por defecto 9 piezas A4 verticales, una etiqueta de 205 × 165 mm y otra de 205 × 95 mm.
- Mantén datos, calendarios, actividades y cuadrícula con base mayormente blanca, pero visualmente RICA. Bajo consumo no significa minimalismo vacío.
- Deriva de las referencias una gramática común: paleta, lettering, motivos, marco, ilustración y componentes. Aplícala a TODAS las páginas.
- Integra al menos tres capas temáticas por interior: cabecera expresiva, estructura funcional tematizada y marco, pie o acento distribuido.
- Usa generación visual para ilustraciones, lettering, marcos, iconos y texturas. Compón nombres, campos, tablas, cuadrículas y fechas con herramientas deterministas.
- Calcula calendarios con biblioteca de fechas; lunes primero por defecto. No inventes feriados.
- Mantén la hoja de datos vacía salvo solicitud expresa. Conserva nombre y acentos exactos donde sí se personaliza.
- Rehaz cualquier página genérica, vacía o resuelta con título plano, miniatura aislada y líneas sueltas.
- No declares `PRINT_READY` sin verificar arte real, resolución efectiva, márgenes, sangrado, encuadernación y color.
- Guarda pedidos, imágenes y datos personales fuera de Git; `design-runs/` permanece local e ignorado. Versiona solamente skills, reglas y conocimiento portable, sin bases SQLite ni archivos pesados.

## Decision Gates

| Condición | Acción |
| --- | --- |
| Referencia vibrante o pedido “vibrante” | Usa perfil `vibrant`: lettering protagonista, marco ilustrado, iconografía, color intenso y personaje integrado. |
| Sin intensidad indicada | Usa `balanced-vibrant`; evita plantillas corporativas austeras. |
| Zona de escritura | Conserva blanco útil y baja opacidad interior; concentra saturación en perímetro, títulos y divisores. |
| Captura con UI o mockup | Extrae solo lenguaje visual; no copies interfaz, guías, precio ni marcas de producción. |
| Calendario o tabla | Genera estructura y texto con código; usa recursos visuales solo como capas decorativas. |

## Execution Steps

1. Valida pedido con [schema](../../schemas/agenda-order.schema.json) y [especificaciones](../../knowledge/agenda-specs.json).
2. Clasifica referencias como contenido, estilo o fondo y crea una mini guía visual.
3. Define un mapa decorativo por pieza usando [interiores vibrantes](references/vibrant-interiors.md).
4. Produce recursos temáticos y maqueta contenido funcional de forma determinista.
5. Renderiza cada pieza y la vista conjunta. Evalúa páginas individualmente al 100 %, no solo como miniaturas.
6. Aplica [reglas visuales](../../standards/agenda-design-rules.md) y completa el [QA](../../templates/agenda-qa.md).

## Output Contract

Entrega piezas separadas, PDF con medidas físicas cuando corresponda, PNG de revisión, vista conjunta, inventario, resolución efectiva, recursos usados y estado `PASS`, `PASS WITH WARNINGS` o `FAIL` por pieza. Expón pendientes de impresión.

## References

- [Interiores vibrantes](references/vibrant-interiors.md)
- [Workflow](../../../workflows/tribe/agenda-design.md)
- [Reglas visuales](../../standards/agenda-design-rules.md)
- [Especificaciones](../../knowledge/agenda-specs.json)
- [Contrato de pedido](../../schemas/agenda-order.schema.json)
- [QA](../../templates/agenda-qa.md)
- [Resiliencia](../../policies/non-blocking-generation.md)
