## Context

AI-Workspace es la fuente compartida de capacidades. Los repositorios reales de SITOP V2 y Tribe Sport no se han identificado en esta tarea. Existe una ampliacion de 18 skills de software sin integrar; no se publicara incidentalmente con este cambio.

## Goals / Non-Goals

Goals: politica SDD aplicable a todas las oficinas de software, OpenSpec operativo en este repo, perfiles reutilizables y evidencia honesta.
Non-goals: instalar Gentle-AI, construir aplicaciones, descubrir repos privados, aprobar formularios o desplegar.

## Decisions

- Usar `spec-driven` y los artefactos nativos proposal/specs/design/tasks; agregar verificacion y trazabilidad como complementos Markdown sin inventar comandos oficiales.
- Guardar OpenSpec en cada producto; no centralizar todos los cambios de las aplicaciones en AI-Workspace. Registrar la revision comun consumida.
- Fijar `@fission-ai/openspec` 1.14.3 y lockfile. La version no obliga a actualizar herramientas existentes sin revision de compatibilidad.
- Mantener `sdd-openspec` como entrada propia; configuraciones generadas del proveedor se instalan en cada destino con el CLI y se inspeccionan antes de versionar.
- SITOP conserva F0-F5; Tribe Sport conserva criterios y evidencia con menor carga documental. Especificaciones y formularios se enlazan por ID para evitar versiones contradictorias.
- No agregar un servicio ni arquitectura de despliegue a una politica documental. UML de producto se define por cambio cuando corresponda.

## Risks / Trade-offs

El CLI valida forma, no verdad ni cobertura de pruebas. La configuracion context/rules es orientacion, no un bloqueo tecnico de implementacion. La aplicacion requiere revisar que los agentes y CI sigan el flujo. Las opciones CLI se comprueban contra la version fijada, ya que la rama main del proveedor evoluciona.

## Migration Plan

Adoptar aqui, probar CLI y publicar conocimiento. Cuando se abra cada aplicacion, inspeccionar su estructura, instalar o reutilizar una version compatible, fusionar configuracion y vincular instrucciones. No ejecutar bootstrap sobre una ruta no proporcionada.

## Open Questions

Faltan rutas de aplicaciones, versiones reales de sus stacks y responsables de aceptacion. Esos datos no impiden definir esta base comun.
