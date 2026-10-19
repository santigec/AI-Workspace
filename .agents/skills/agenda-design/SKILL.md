---
name: agenda-design
description: "Trigger: agenda, planner, interiores de agenda. Genera conjuntos A4 temáticos, vibrantes, funcionales y listos para revisión de impresión."
license: Apache-2.0
metadata:
  author: santigec
  version: "0.2.0"
---

## Activation Contract

Activa este skill para crear o adaptar agendas, planners, calendarios, hojas de datos, actividades, cuadrículas y sus etiquetas.

## Hard Rules

- Lee primero [el skill de dominio](../../../tribe/skills/agenda-design/SKILL.md) y todas sus referencias obligatorias.
- Genera el conjunto completo solicitado; no sustituyas arte final por un brief.
- Calcula calendarios con código. Nunca uses fechas dibujadas por un modelo generativo.
- Conserva el nombre exacto y no rellenes la hoja de datos salvo petición expresa.
- Trata “bajo consumo” como fondo mayormente blanco, NO como minimalismo vacío.

## Decision Gates

| Entrada | Acción |
| --- | --- |
| Hay referencias | Extrae su lenguaje visual y aplica su intensidad a cada interior. |
| Se pide estilo vibrante | Usa el perfil `vibrant` de la referencia visual del skill. |
| No se define intensidad | Usa `balanced-vibrant`; evita plantillas austeras. |

## Execution Steps

1. Clasifica referencias como contenido, estilo o fondo.
2. Define un sistema visual común antes de maquetar.
3. Compón cada página según su función con arte temático integrado.
4. Renderiza, inspecciona cada pieza a tamaño legible y corrige.
5. Valida fechas, medidas, texto, escritura útil y continuidad visual.

## Output Contract

Entrega piezas separadas, vista conjunta, inventario, estado de QA y advertencias de impresión.

## References

- [Contrato completo](../../../tribe/skills/agenda-design/SKILL.md)
