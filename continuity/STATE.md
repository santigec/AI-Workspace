# Continuidad — 2026-10-19

## Prioridad
Sincronizar conocimiento: skills, reglas, pruebas técnicas y memoria Engram, no trabajos pesados. Repo privado santigec/AI-Workspace, rama develop. Proyecto Engram fijo ai-workspace. Importar .engram después del pull, consultar contexto y guardar decisiones antes de exportar/push. No se sincroniza todo el chat automáticamente.

Versión ligera v0.4.1 reemplaza la incorporación pesada v0.4.0 retirada del historial a petición expresa. design-runs se conserva local e ignorado. Los objetos LFS ya recibidos por GitHub pueden seguir ocupando cuota aunque no sean alcanzables; no se elimina ni recrea el repositorio.

## Equipo operativo v0.5.0

Primer equipo de Tribe definido en .codex/agents: coordinador, disenador y revisor. Se aplican los 21 skills existentes, no se añaden skills por cada rol. Workflow: workflows/tribe/operating-team.md; explicación: docs/operating-team.md. Activación por petición del usuario para una tarea concreta; no es una oficina autónoma en segundo plano ni dashboard web.

El hilo principal coordina brief -> ejecución -> revisión independiente y correcciones. Los perfiles heredan modelo/permisos, sin imponer otros. Para la prueba inicial los perfiles se cargan explícitamente por encargo; no afirmar validación del descubrimiento nativo hasta abrir una sesión que los detecte. Memoria centralizada en el padre puede pasarse a los subagentes sin volver a abrir SQLite bloqueada por sandbox. Solo conocimiento/informes ligeros a Git y Engram.

Prueba de tres delegaciones reales completada el 2026-10-19: revisión de una hoja cuadriculada K-pop existente, sin editar/generar. Coordinador entregó brief, diseñador midió/inspeccionó y revisor verificó independientemente: PASS digital de esa pieza sin correcciones obligatorias. Informe: evals/teams/operating-team-2026-10-19.md. No valida descubrimiento nativo de perfiles, otras diez piezas ni impresión. Tres TOML parseados, estructura del workspace y 43 pruebas técnicas PASS.

## Conocimiento

- v0.5.2: CodeGraph @colbymchenry/codegraph1.6.2 local fijado y MCP registrado en este Codex con solo codegraph_explore. Launcher scripts/codegraph.mjs y configurador scripts/configure_codegraph.py portables por ubicacion del repo; cada equipo debe ejecutar npm ci/configuracion propia. Indice local AI-Workspace generado y excluido de Git. Skill codegraph-navigation0.1.0, sdd-openspec0.1.1 y24skills registrados. Politica software-office/standards/codegraph.md. Cada aplicacion requiere indice propio y acceso a reglas; no basta mencionar el repo. La sesion abierta puede requerir recargar MCP; no afirmar herramienta nativa cargada por solo cambiar config. No inicializado SPI ni repositorios de aplicaciones. No medir ahorro de tokens sin comparativa.

- SDD + OpenSpec obligatorio para todo desarrollo de software por decision del usuario del 2026-10-19. Politica software-office/standards/sdd-openspec.md y entrada sdd-openspec 0.1.0; herramientas locales OpenSpec 1.14.3 con lockfile. SITOP V2 mantiene Spring Boot/Angular y F0-F5; Tribe Sport mantiene Django/Railway con documentacion ligera y la misma trazabilidad. Cada producto conserva openspec/ junto al codigo; AI-Workspace guarda reglas comunes. No se instala Gentle-AI por esta decision. Validacion estructural y archivo no equivalen a pruebas, aceptacion ni autorizacion de produccion. Instalacion/configuracion en aplicaciones y perfiles especializados siguen pendientes.
- Registro ampliado a 23 skills alpha en v0.5.1 (mug-box-design y sdd-openspec agregados); los 18 borradores locales de software anteriores siguen fuera del registro y de esta publicacion. Los recuentos de 21 mas abajo describen la base v0.5.0.
- Adopcion SDD ejecutada en el propio workspace: seis tests reales de OpenSpec PASS, 43 tests Python y registro PASS sobre alcance publicable aislado. Cambio adopt-sdd-openspec archivado el 2026-10-19; cinco requisitos vigentes en openspec/specs/software-sdd/spec.md, validacion estricta y tareas archivadas PASS. Las dos evaluaciones de comportamiento de sdd-openspec siguen NOT_RUN. Base publicada en ffb621a, cierre y consolidacion en commit posterior. Los repositorios de aplicaciones y sus agentes no se han inicializado por esta entrega.

- Ampliación local 2026-10-19: mug-box-design 0.1.0 para cajas de taza 150 × 200 mm, composición plana continua, artes inferiores laterales y reserva central inferior sin protagonistas (solo fondo discreto). Tema anclado a 120 mm desde base/80 mm desde arriba, borde completo temático, paleta y lettering del tema. Reserva exacta y plantilla física pendientes por pedido; dos casos visuales NOT_RUN. Registro local ampliado; no confundir los cambios sin publicar con la versión v0.5.0.
- 21 skills de dominio, wrappers .agents/skills no contados dos veces. Todos alpha. Registro registry/skills.yaml. Agenda-design0.1.4, última revisión visual v0.3.4.
- Engram guarda decisiones, correcciones e índice de skills; las instrucciones completas permanecen en SKILL.md. continuity/memory-topics.json es la instantánea de carga inicial; no resembrar de rutina si las memorias evolucionaron.
- Taza205x95mm. Tomatodo500ml232x125mm,600ml232x142mm,750ml232x182mm. Arte plano continuo adaptado.
- Agenda: nueve modelos A4 vertical210x297mm y etiquetas205x165/205x95mm. Años por fecha del usuario; pruebas2026/2027 lunes primero sin feriados.
- Portadas solo tema/nombre solicitado, sin Agenda/año/frases por defecto. Etiquetas vivas adaptadas al tema sin inferir género por nombre.
- Datos importantes sin frases, nombres ni valores prellenados. Interiores blancos con jerarquía profesional.
- Cuadrícula: cabecera ilustrada/lettering temático elaborado, no texto común más miniatura; sin títulos funcionales ni Tema/Fecha. Pie coordinado, escritura amplia y marca de agua central tenue.

## Pruebas y límites
Última muestra local: agenda-kpop-2026-10-15-v2; cabecera HUNTR/X ilustrada2172x724px (~284ppp al ancho194mm). Portadas ~127ppp originales. No arrastrar Cele: fue otro pedido. Muestras y scripts de pedidos permanecen locales y no se transfieren al clonar esta versión ligera.

La validación técnica no certifica impresión. Casos visuales formales siguen NOT_RUN. Faltan prueba física, sangrado y encuadernación antes de PRINT_READY. En el segundo equipo seguir docs/two-computers.md; falta ejecutarse allí, no afirmar conexión ni MCP activo.
