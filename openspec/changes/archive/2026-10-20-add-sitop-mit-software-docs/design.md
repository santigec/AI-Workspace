## Context

El formato MIT/SITOP ya se probó en SPI Generator; el usuario pide centralizar las reglas en AI-Workspace y publicar sus skills/versiones. Los membretes son privados y la política del workspace excluye binarios.

## Decisions

Skill específica de oficina en software-office/skills, con nombre registrable y acceso .agents. Separar contenido/trazabilidad de geometría y recursos. Reutilizar helper sin modificar su comportamiento. Referencias MIT locales .tools/sitop-mit y manifiesto SHA256 para restauración explícita en otro equipo. Sin copiar el generador específico SPI ni fijar su stack/IDs/rutas. Versionar 0.1.0 alpha, workspace 0.5.6. Inventario derivado del registro actual; no contabilizar wrappers ni skills personales.

## Risks / Trade-offs

Git no lleva los membretes: el segundo equipo debe restaurarlos. Evaluación de la nueva skill en segundo producto pendiente; no afirmar estabilidad ni instalación automática. Las aprobaciones institucionales permanecen humanas.

## Verification

Validar estructura/registro, enlaces, OpenSpec y manifiesto local; comprobar helper por identidad con versión previamente probada y smoke sintético. Diff y staged explícitos; sin binarios. Publicar únicamente develop de AI-Workspace.
