# Continuidad — 2026-10-19

## Prioridad
Sincronizar conocimiento: skills, reglas, pruebas técnicas y memoria Engram, no trabajos pesados. Repo privado santigec/AI-Workspace, rama develop. Proyecto Engram fijo ai-workspace. Importar .engram después del pull, consultar contexto y guardar decisiones antes de exportar/push. No se sincroniza todo el chat automáticamente.

Versión ligera v0.4.1 reemplaza la incorporación pesada v0.4.0 retirada del historial a petición expresa. design-runs se conserva local e ignorado. Los objetos LFS ya recibidos por GitHub pueden seguir ocupando cuota aunque no sean alcanzables; no se elimina ni recrea el repositorio.

## Equipo operativo v0.5.0

Primer equipo de Tribe definido en .codex/agents: coordinador, disenador y revisor. Se aplican los 21 skills existentes, no se añaden skills por cada rol. Workflow: workflows/tribe/operating-team.md; explicación: docs/operating-team.md. Activación por petición del usuario para una tarea concreta; no es una oficina autónoma en segundo plano ni dashboard web.

El hilo principal coordina brief -> ejecución -> revisión independiente y correcciones. Los perfiles heredan modelo/permisos, sin imponer otros. Para la prueba inicial los perfiles se cargan explícitamente por encargo; no afirmar validación del descubrimiento nativo hasta abrir una sesión que los detecte. Memoria centralizada en el padre puede pasarse a los subagentes sin volver a abrir SQLite bloqueada por sandbox. Solo conocimiento/informes ligeros a Git y Engram.

Prueba de tres delegaciones reales completada el 2026-10-19: revisión de una hoja cuadriculada K-pop existente, sin editar/generar. Coordinador entregó brief, diseñador midió/inspeccionó y revisor verificó independientemente: PASS digital de esa pieza sin correcciones obligatorias. Informe: evals/teams/operating-team-2026-10-19.md. No valida descubrimiento nativo de perfiles, otras diez piezas ni impresión. Tres TOML parseados, estructura del workspace y 43 pruebas técnicas PASS.

## Conocimiento
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
