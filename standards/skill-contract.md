# Contratos de skills

Un contrato especifica entradas, salidas y condiciones de terminación. Los tres skills del flujo de impresión incorporan contratos en su SKILL.md.

## Entradas

Distingue campos requeridos y opcionales. Un dato ausente no se sustituye por un ejemplo del repositorio. Expresa dimensiones con unidades y registra la fuente de las especificaciones.

## Salidas

Usa campos explícitos, aunque el resultado sea Markdown:
- status: PASS, PASS WITH WARNINGS o FAIL.
- evidence: observaciones o mediciones que sustentan el resultado.
- warnings: limitaciones no críticas.
- missing_inputs: datos o recursos pendientes.
- next_skill: identificador de un skill del registro, o null.
- artifact: ruta del archivo producido, o null si no se produjo.

FAIL incluye una operación bloqueada por datos críticos ausentes. Indica reason: missing_input, unsupported_operation o requirement_failed. Un diagnóstico puede pasar su contrato de análisis sin que el arte sea apto para imprimir.

PASS WITH WARNINGS solo aplica si todos los requisitos críticos de esa etapa están verificados. Ningún warning habilita una entrega de producción con medidas, márgenes, espejo o resolución críticos pendientes.

## Versiones y compatibilidad

[registry/skills.yaml](../registry/skills.yaml) es la fuente de versiones, estado y propietario. No se añaden campos no compatibles al frontmatter de los skills.
Estados: experimental, alpha, beta, stable, deprecated. Esta versión mantiene todos los skills en alpha porque no hay evidencia de producción.
Una revisión cambia la versión del skill afectado; una versión del repositorio no cambia automáticamente todos los skills.

## Dependencias

requires_before indica evidencia requerida antes de una etapa; recommends_next indica continuidad posible. Mantenerlos separados evita ciclos artificiales entre layout y QA.
