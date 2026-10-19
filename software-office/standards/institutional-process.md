# Proceso institucional de desarrollo de software

Este baseline traduce el contenido de seis formularios institucionales a un flujo trazable para desarrollo y modificación de software. Su adopción responde a la regla del usuario para este workspace. Elaborar un plan o una plantilla no autoriza desplegar, aceptar ni firmar en nombre de responsables.

La fuente de nombres, hashes, etiquetas y límites es [institutional-forms.json](../knowledge/institutional-forms.json). Las [plantillas vacías](../templates/forms/00-request.md) conservan las etiquetas; son representaciones de contenido y estructura, cuya maquetación no ha sido validada mediante render.

| Etapa | Entrada | Artefacto y evidencia necesarios | Responsable indicado por la fuente |
|---|---|---|---|
| Solicitud F0 | Necesidad y proceso afectado | [Solicitud](../templates/forms/00-request.md), código del requirente, justificación, alcance y proceso adjunto | Área requirente y solicitante con cargo/firma |
| Especificación F1 | F0 y aclaraciones | [RFS](../templates/forms/01-rfs.md), prioridad, reglas, flujos, escenarios y requisitos no funcionales; revisión/aprobación reales | DTIC asigna código después de priorización; comité informático define prioridad; equipo conformado realiza/revisa/aprueba |
| Estimación F2 | RFS y prioridades | [Estimación](../templates/forms/02-estimation.md), equipo, método, backlog inicial priorizado con fechas e impactos | Analistas de desarrollo designados; stakeholders del requirente; Product Owner, Development Team, Scrum Master si corresponde al método |
| Plan QA F3 | Requisitos y escenarios | [Guion QA](../templates/forms/03-qa-plan.md) por funcionalidad, entradas, iteraciones, adjuntos y resultados esperados | Analista de Desarrollo de Sistemas realiza; Coordinador de Desarrollo de Sistemas revisa |
| Aceptación F4 | Versión candidata, F3 y evidencias | [Pruebas y aceptación](../templates/forms/04-acceptance.md), matriz de historias/criterios, resultado esperado, aprobación y observaciones; resumen Si/No y declaración reales | Identificar al requirente autorizado; bloques realizado/verificado/aprobado y cargo/firma del formato |
| Liberación F5 | Versión aceptada y cambio autorizado | [Paso a producción](../templates/forms/05-production-release.md), ticket, precondiciones, respaldo, instalación, rollback, verificación, autorización y ejecución | Infraestructura para respaldo/instalación/rollback; administrador de aplicación para verificar; solicitante/revisor/aprobador y ejecutor identificados |

Mantener un identificador de caso que relacione F0–F5 y referencias explícitas entre requisitos, backlog, escenarios, evidencias y versión candidata. Los códigos son campos del caso: el de solicitud, el registrado por DTIC, el de documento QA, el de pruebas y el de paso a producción no se deben confundir con versión de plantilla. No se detectó versión documental explícita: `source_version: null`.

## Controles de transición

Completar y revisar la solicitud antes de fijar la RFS. Registrar la prioridad y el código cuando corresponda al proceso institucional. La RFS explicita entradas, salidas, validaciones, pantallas/reportes, reglas, escenarios, precondiciones, flujos principales/alternos/excepciones, base legal, restricciones y requisitos no funcionales.

La estimación contiene fechas previstas y análisis de infraestructura, funcionalidad, seguridad, rendimiento y otros impactos. SCRUM es recomendación del original ante incertidumbre, no obligación universal deducida de la plantilla. Las direcciones concretas prellenadas en la instancia no son participantes universales. Horas, puntos, costo, rangos, supuestos, dependencias e incertidumbre son complementos técnicos identificados, sin convertirlos en columnas oficiales.

El plan QA define el resultado esperado antes de ejecutar. Adjuntar resultados reales, datos usados, versión, entorno y reportes como evidencia complementaria según [política de evidencia](evidence-policy.md). Resolver defectos o registrar disposición por responsable autorizado antes de proponer aceptación. Un build o test exitoso no equivale a aceptación funcional del requirente.

La aceptación exige decisión real y evidencia vinculada a la versión candidata. Casillas, fechas, nombres y firmas permanecen vacíos hasta obtener datos confirmados. No inferir aprobación de una tarea, una ejecución automatizada, texto declarativo, un cargo escrito ni marcas de la instancia fuente. Registrar pendientes y quién debe resolverlos. La declaración F4 solicita liberación, pero no reemplaza la autorización F5.

Control original F5:

> La aplicación del paso a producción en ambientes productivos, deberá generarse fuera de horario laboral; excepto para cambios emergente que deberán ser expresamente autorizados por la Dirección de Tecnologías de la Información. De ser necesario se deberá gestionar la correspondiente ventana de mantenimiento.

Preparar respaldo identificado, procedimiento secuencial, rollback y verificación por el administrador. Si aparecen errores, el original dispone reemplazar el último respaldo de producción con el anterior vigente respaldado antes del cambio y verificar operación. Precisar el procedimiento del caso y sus consecuencias antes de ejecutar. No ejecutar cambios productivos a partir de esta regla genérica: debe existir autorización de la acción concreta y los registros institucionales aplicables. Versión/tag/hash, migraciones, configuración, secretos y pruebas de recuperación pertenecen al expediente técnico complementario.

## Fidelidad y límites

- F3 conserva `FIRMAS DEL ÁREA REQUIRENTE`, aunque sus cargos impresos son de Desarrollo.
- F4 conserva dos secciones numeradas `3.-`. El archivo se denomina Requirente, pero la instancia prellenada usa cargos DTI; identificar y documentar al representante requirente autorizado sin asumir equivalencia.
- F0 y F4 contienen casos prellenados. Las plantillas omiten personas, contenido del caso, códigos y marcas. Los campos de firma no producen una firma.
- F2 no contiene esfuerzo numérico ni costo. Un ADR, modelado de arquitectura, evidencia CI, análisis de seguridad o estimación numérica son complementos técnicos y se deben distinguir del formulario oficial.
- F0–F4 se extrajeron directamente de OOXML; membretes institucionales inspeccionados sin copiarlos. F5 se extrajo del DOC binario mediante CFB/FIB/CLX después de denegación Word COM, y se cotejó con PDF auxiliar separado. No se certifican geometría, celdas fusionadas, glifos checkbox ni numeración automática del DOC.
- Ningún PDF V1 establece versión de los originales. No se validó maquetación mediante render ni se incorporan logos, binarios ni extracciones personales al baseline.

Las etiquetas exactas y controles específicos por formulario se comprueban con el manifiesto. Cuando falte un dato, consignar el pendiente en el expediente del caso; no completar con ejemplos prellenados, aprobaciones supuestas o valores inventados.
