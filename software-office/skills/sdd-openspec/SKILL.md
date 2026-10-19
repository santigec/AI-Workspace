---
name: sdd-openspec
description: Gestiona desarrollo de software mediante especificaciones OpenSpec, desde propuesta y escenarios hasta tareas, pruebas y archivo, con perfiles para SITOP V2 y Tribe Sport.
---

# SDD con OpenSpec

Aplica al iniciar, implementar, revisar o retomar cambios de software de las oficinas. Lee [politica comun](../../standards/sdd-openspec.md), [workflow](../../../workflows/software-office/sdd-openspec.md) y [adopcion por repositorio](../../../docs/sdd-openspec.md).

En exploracion estructural aplicar [CodeGraph](../../standards/codegraph.md) si esta disponible e indexado, con proyecto explicito y contexto acotado. No sustituye escenarios, pruebas ni lectura de configuracion/documentacion no cubierta.

Evaluar UML afectado en cada cambio y aplicar [modelado](../uml-modeling/SKILL.md) y [renderizado](../uml-rendering/SKILL.md) cuando corresponda. Actualizar fuentes, referencias y graficos o justificar no afectacion; comprobar deriva y revisar semantica antes de completar tareas.

1. Identifica repositorio y perfil, instrucciones existentes, estado Git, stack/versiones, OpenSpec instalado y specs/cambio activo. No inicies un cambio duplicado ni presentes conducta no inspeccionada como vigente. Si no hay acceso al repositorio de la aplicacion, prepara la especificacion y declara que la integracion de ese destino sigue pendiente.
2. Antes de implementar, construye o revisa proposal, specs con IDs y escenarios, design proporcional y tasks. Especifica limites y resultados observables; resuelve con el usuario solo decisiones necesarias aun no autorizadas, mientras avanzas en lo independiente.
3. En SITOP V2 enlaza F0-F5 y sus controles vigentes; en Tribe Sport usa expediente ligero, Django/Railway y direccion visual del proyecto. No conviertas los formularios de SITOP en requisito universal ni elimines trazabilidad por aligerar documentos.
4. Implementa desde tareas y escenarios. Actualiza primero los artefactos si cambia el comportamiento acordado. Comprueba integracion, permisos, datos y fallos relevantes; aplica skills especializados disponibles sin afirmar que estan instalados si no lo estan.
5. Ejecuta validacion estructural OpenSpec y pruebas apropiadas del codigo. Usa el [informe complementario](../../templates/openspec/verification.md) para relacionar requisito, tarea, implementacion, prueba, resultado y evidencia/version. No confundir validacion de Markdown con pruebas de aplicacion, ni simulaciones con infraestructura real.
6. Revisa el diff y evidencia antes de completar tareas y archivar. Registra pendientes, decisiones y version comun consumida. Archivo, aceptacion y despliegue son estados distintos. No inventes firmas ni permisos de produccion.

Usa el CLI local y su `--help` de la version fijada; no inventes comandos slash. En este repo `npm run openspec -- <argumentos>` ejecuta la dependencia local. En otros repositorios revisa primero su gestor y convenciones. La configuracion no bloquea tecnicamente el codigo: verificar cumplimiento requiere revision y pruebas.
Los artefactos de cada aplicacion pertenecen a su repo; las reglas reutilizables a AI-Workspace. Conserva evidencia ligera, excluye secretos/binarios y evita copiar una referencia privada como si garantizara acceso desde otro chat.
