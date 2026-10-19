# SDD con OpenSpec

Regla comun solicitada por el usuario el 2026-10-19 para **todo desarrollo de software** gobernado por AI-Workspace: SITOP V2, Tribe Sport y futuras oficinas. No aplica el expediente de software a pedidos de sublimacion o agendas.

## Fuente de verdad y orden de trabajo

Antes de implementar un cambio de comportamiento, explorar el codigo y las especificaciones vigentes; registrar objetivo, alcance, exclusiones y decisiones pendientes. Crear un cambio OpenSpec en el repositorio del producto con `proposal.md`, deltas en `specs/`, `design.md` y `tasks.md` usando el schema `spec-driven`. Trabajar desde la especificacion acordada y la autorizacion existente del usuario; no exigir otra confirmacion rutinaria si el encargo ya define lo necesario. Las decisiones de negocio sin respuesta quedan pendientes y no se implementan como hechos.

Cada requisito tiene identificador estable y escenarios observables: exito, validacion, errores, permisos y no funcionales segun corresponda. En archivos OpenSpec conservar encabezados `Requirement`/`Scenario`, SHALL o MUST y WHEN/THEN exigidos por la herramienta; el resto del texto puede estar en espanol. Una descripcion retrospectiva sin inspeccion no es evidencia del comportamiento vigente.

El diseno registra contratos/API, datos/migraciones, seguridad, experiencia y compatibilidad afectados. Incluir UML en fuente editable cuando aporte al caso: casos de uso/actividad para flujos, secuencia para interacciones, clases para dominio y componentes/despliegue para arquitectura. Justificar los diagramas no aplicables; no producir todos por rutina para una correccion menor.

Dividir tareas por entregable verificable. Relacionar requisito -> tarea -> codigo -> prueba -> evidencia/version. Si la implementacion descubre un cambio de comportamiento necesario, actualizar primero el delta y el diseno afectados. No ampliar silenciosamente el alcance.

Para cambios pequenos, usar artefactos breves pero suficientes. Refactorizaciones o documentacion sin comportamiento nuevo deben explicitarlo y verificar que no haya regresion; no inventar requisitos funcionales. Cualquier excepcion del CLI se usa solo si la version instalada la soporta y el caso lo justifica.

## Dos perfiles documentales

| Perfil | Stack previsto | Aplicacion del proceso |
|---|---|---|
| SITOP V2 | Java Spring Boot + Angular | OpenSpec + formularios institucionales F0-F5 aplicables, UML y evidencia trazable; aprobaciones por sus responsables reales |
| Tribe Sport | Python Django + Railway | OpenSpec + diseno proporcional, pruebas y registro de liberacion; F0-F5 no obligatorios |

En SITOP vincular solicitud/propuesta con F0, requisitos con F1, tareas/estimacion con F2, escenarios/plan QA con F3, aceptacion con F4 y liberacion con F5. Los formularios y specs deben referenciar los mismos IDs y version del caso; registrar discrepancias antes de tratar una copia como vigente. OpenSpec no sustituye firmas, priorizacion, aceptacion ni autorizacion de produccion.
Tribe Sport conserva las mismas exigencias de comportamiento verificable y evidencia; solo reduce formularios. Su identidad visual se consulta en el conocimiento de marca disponible del proyecto, sin imponerla a SITOP.

## Verificacion y cierre

Ejecutar `openspec validate --all --strict --no-interactive` desde el repositorio correcto. Revisar tambien tareas, trazabilidad, coherencia del codigo y pruebas pertinentes realmente ejecutadas. La validacion de OpenSpec es estructural; no demuestra pruebas, seguridad, aceptacion humana ni despliegue.
Registrar comando, entorno, version/commit, resultado real, pruebas omitidas y defectos pendientes en un informe complementario de verificacion. PASS, FAIL, SKIPPED y NOT_RUN son distintos; un checklist marcado no sustituye reportes. No marcar tarea completa antes de su entregable y verificacion.
Archivar el cambio cuando haya implementacion y revision suficientes, consolidando deltas en `openspec/specs/` y revisando el diff. Una especificacion vigente no es una propuesta pendiente. No usar `--no-validate`, tareas ficticias o archivos vacios para obtener un estado verde. Archivar no autoriza produccion: F4/F5 o la aceptacion correspondiente siguen teniendo sus controles propios.

## Repositorios, agentes y memoria

Cada aplicacion conserva `openspec/` con su codigo y evidencia ligera. AI-Workspace conserva esta politica, skills y configuraciones de referencia. Registrar el commit de AI-Workspace utilizado; no copiar wrappers que pierdan sus referencias relativas ni suponer acceso automatico entre repositorios.
Coordinacion identifica el cambio y responsables; analisis prepara propuesta/specs; arquitectura prepara diseno; desarrollo aplica tareas; QA verifica escenarios y regresiones con independencia cuando el riesgo lo requiera. La existencia de esta politica no crea perfiles de agentes ni activa delegacion por si sola.
Engram guarda decisiones comunes bajo `ai-workspace` y decisiones del producto bajo su proyecto correspondiente. Consultar codigo, specs y evidencia al reanudar; Git transporta archivos y exportaciones de memoria explicitamente, no sincroniza sesiones en segundo plano.

## Herramientas

Version comprobada aqui: OpenSpec **1.14.3** fijada en `package.json` y `package-lock.json`; Node compatible segun `engines` del paquete (>=20.19.0 para esa version). Preferir dependencia local del proyecto; revisar gestor/lockfile existente antes de instalar. Inicializar/configurar cada repositorio destino y revisar los archivos generados; no modificar configuracion global por defecto.
`context` y `rules` de OpenSpec orientan al agente: no son un control tecnico que impida saltarse etapas. Aplicar esta politica tambien mediante revision del cambio y controles CI apropiados al proyecto. No instalar Gentle-AI como consecuencia de esta adopcion.

Fuentes oficiales consultadas el 2026-10-19: [OpenSpec](https://github.com/Fission-AI/OpenSpec), [CLI](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md), [configuracion](https://github.com/Fission-AI/OpenSpec/blob/main/docs/customization.md). Las instrucciones de AI-Workspace son una adaptacion propia; no una copia ni una certificacion del proveedor. La documentacion de main puede evolucionar: comprobar comandos en la version fijada.
