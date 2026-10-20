---
name: adhesivo-tarrito
description: Crea arte envolvente de 180 x 80 mm con cuatro paneles de 45 x 80 mm para adhesivo tarrito y etiqueta tarrito.
---

# Adhesivo tarrito en AI-Workspace

## Activation Contract

Activa este acceso para pedidos de adhesivos envolventes de tarritos cuadrados.

## Hard Rules

- Lee y aplica el [skill de dominio](../../../tribe/skills/adhesivo-tarrito/SKILL.md) y todas sus referencias.
- Genera y muestra el arte cuando se solicite; no sustituyas la imagen por una ficha.
- Conserva 180 x 80 mm y los cuatro paneles conceptuales de 45 x 80 mm sin inventar parametros de produccion.

## Decision Gates

| Pedido | Accion |
|---|---|
| Generacion | Sigue el flujo del skill de dominio. |
| Produccion | Exige plantilla y QA confirmados. |

## Execution Steps

1. Carga el skill de dominio.
2. Ejecuta su workflow y QA.
3. Muestra el archivo real y sus limitaciones.

## Output Contract

Devuelve imagen visible, archivo, medidas, revision por panel y estado de produccion justificado.

## References

- [Skill de dominio](../../../tribe/skills/adhesivo-tarrito/SKILL.md)
