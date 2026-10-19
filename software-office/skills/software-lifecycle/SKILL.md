---
name: software-lifecycle
description: Coordinar el ciclo institucional de desarrollo o modificación de software Java Spring Boot desde solicitud hasta liberación, con seis formularios y evidencia trazable.
---

# Ciclo de ingeniería de software

Alcance: coordinar una entrega completa o ubicar el estado real de una modificación. Entrada: objetivo del usuario, repositorio, identificador del caso, formularios y evidencias existentes.

Leer el [proceso institucional](../../standards/institutional-process.md) y el [baseline de formularios](../../knowledge/institutional-forms.json). Seguir el [workflow de ingeniería](../../../workflows/software-office/engineering-lifecycle.md) para ordenar requisitos, estimación, implementación, QA, aceptación y preparación de producción. No rehacer etapas ya sustentadas por evidencia vigente.

1. Identificar el caso, responsables, versión candidata y pendientes. Relacionar F0–F5 sin confundir sus códigos.
2. Completar la [solicitud F0](../../templates/forms/00-request.md) y coordinar RFS, estimación, plan QA, aceptación y liberación con los skills especializados del workspace según el trabajo solicitado.
3. Mantener trazabilidad de requisito a implementación, prueba, evidencia y versión. Distinguir campos originales de complementos técnicos como ADR, esfuerzo numérico y reportes CI.
4. Entregar expediente revisable con estado de cada etapa, evidencias existentes, bloqueos concretos y siguiente responsable.

Las plantillas son vacías y no constituyen aprobaciones. No heredar datos ni marcas de los casos fuente, inventar firmas o llamar aceptado a un build exitoso. El baseline es una regla de trabajo solicitada por el usuario; no autoriza despliegue actual. Conservar las inconsistencias documentadas en F3/F4 y declarar que la maquetación original no fue validada.
