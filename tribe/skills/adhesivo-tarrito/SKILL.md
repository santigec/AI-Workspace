---
name: adhesivo-tarrito
description: Genera arte envolvente de 180 x 80 mm en cuatro paneles centrados para adhesivo tarrito, etiqueta tarrito y frasco cuadrado.
---

# Adhesivo tarrito

## Activation Contract

Activa este skill para crear o adaptar el adhesivo envolvente de un tarrito cuadrado de 45 x 45 x 80 mm. Carga las [reglas de composicion](../../standards/adhesivo-tarrito-rules.md), el [workflow](../../../workflows/tribe/adhesivo-tarrito.md) y el [QA](../../templates/adhesivo-tarrito-qa.md).

## Hard Rules

- Produce un unico arte plano y continuo de **180 x 80 mm**, dividido conceptualmente en cuatro paneles contiguos de **45 x 80 mm**: P1 [0,45), P2 [45,90), P3 [90,135) y P4 [135,180] mm.
- Centra en cada panel un foco tematico legible. Distribuye motivos, articulos y figuras secundarios sin poner texto, rostros, logos ni detalles criticos sobre las uniones x = 45, 90 y 135 mm.
- Mantiene un fondo continuo y transiciones coordinadas entre paneles; no entrega cuatro imagenes aisladas, un mockup ni una perspectiva del tarrito.
- Adapta el caracter visual solicitado —masculino, femenino, delicado, divertido u otro— sin inferir genero por nombres ni imponer estereotipos.
- No inventa sangrado, solape, margen seguro, tolerancia, marcas de corte ni plantilla fisica. Mantiene el resultado como DRAFT mientras esos datos no esten confirmados.
- Cuando se solicite el diseno, genera y muestra el arte real; un prompt, brief u orden no completa la solicitud.

## Decision Gates

| Situacion | Accion |
|---|---|
| Arte nuevo | Usa image-generation y conserva la geometria de paneles en el brief. |
| Editar o preservar referencia | Usa image-analysis e image-editing; exige el original accesible. |
| Fidelidad exacta de logo o tipografia | Usa el recurso original o declara la limitacion. |
| Plantilla del proveedor disponible | Verifica medidas y ajusta solo los parametros confirmados. |

## Execution Steps

1. Recoge tematica, textos exactos, referencias y caracter visual; no heredes nombres de otros pedidos.
2. Compone primero el fondo continuo y luego cuatro focos centrados, variando motivos secundarios para dar ritmo sin romper la unidad.
3. Revisa cada panel de forma independiente y el envolvente completo; elimina UI comercial y contenido no solicitado.
4. Genera, inspecciona y muestra el archivo. Registra dimensiones reales, resolucion efectiva y cualquier pendiente de produccion.
5. Aplica print-ready-qa solo con plantilla y parametros confirmados; nunca declares PRINT_READY por apariencia.

## Output Contract

Entrega imagen visible, archivo descargable, 180 x 80 mm, cuatro paneles 45 x 80 mm, resolucion efectiva, textos usados, decisiones visuales y estado DRAFT/PRINT_READY justificado. No incluyas guias visibles salvo solicitud.

## References

- [Reglas de composicion](../../standards/adhesivo-tarrito-rules.md)
- [Workflow](../../../workflows/tribe/adhesivo-tarrito.md)
- [Checklist QA](../../templates/adhesivo-tarrito-qa.md)
- [Catalogo del producto](../../knowledge/product-catalog/jars.yaml)
