# Verificacion de UML mantenido y graficado

Fecha: 2026-10-19. Candidato: base4091b63 mas diff UML acotado. Herramientas locales: PlantUML1.2026.9, Mermaid CLI12.0.0, Chrome local y Temurin21.0.12.1+1 bajo .tools/uml, sin cambiar JAVA_HOME ni el Java8 del sistema. JAR y runtime descargados con los SHA256 fijados; npm con lockfile y scripts de instalacion deshabilitados.

## Evidencia ejecutada

| Control | Resultado |
|---|---|
| Setup y ejecucion real del JAR y Mermaid CLI | PASS |
| Siete modelos PlantUML y tres Mermaid en SVG y PNG | PASS: 10 fuentes, 20 artefactos locales |
| `uml.py check` de esos modelos | CURRENT_HASHES, errores cero; semantica no certificada |
| Revision visual de contacto con los diez PNG | Sin recortes ni solapamientos importantes observados; ejemplos legibles con actores, relaciones, notas y alternativas |
| PlantUML invalido | Rechazado; sin estado de render exitoso |
| Mermaid invalido | Rechazado; sin estado de render exitoso |
| Fixture real con codigo referenciado modificado | check STALE; render bloqueado con modelo igual hasta nota de revision concreta; nuevo render/check correctos |
| `test_uml.py` | PASS: 12 pruebas de deriva de fuentes/codigo/herramientas/artefactos, rutas, referencias y nota de revision |
| Suite Python del alcance publicable | PASS: 60, incluye las 12 anteriores |
| Regresion OpenSpec y perfiles | PASS: 6 pruebas CLI reales |
| Registro y enlaces del alcance publicable | PASS |
| Validacion estricta de specs/cambio OpenSpec | PASS |
| Revision de archivos preparados en Git | Sin PNG, SVG, ZIP, JAR, EXE ni DB |

Las pruebas Python de estructura se ejecutaron en una copia de los archivos versionados y el alcance UML seleccionado; los 17 borradores de software anteriores aun sin registrar quedan fuera de esa copia y publicacion. El validador completo del checkout conserva esos 17 pendientes sin errores nuevos de UML. Se integro el borrador uml-modeling como parte explicita de esta solicitud.

Los graficos locales estan en outputs/uml y la hoja de inspeccion en outputs/uml/contact-sheet.png, fuera de Git. Fuentes, inventario, toolchain y estado ligero permiten regenerarlos. La primera ejecucion Mermaid dentro del sandbox no pudo iniciar Chrome; la ejecucion autorizada fuera de ese limite renderizo correctamente, sin desactivar el sandbox de Chrome. Java8 no ejecutaba el JAR; el runtime local compatible resolvio la incompatibilidad.

## Trazabilidad y limites

UML-001: skills de modelado/render, fuentes editables y herramientas oficiales fijadas. UML-002: renderizadores reales, casos invalidos y revision visual de las muestras. UML-003: manifiesto/check y pruebas unitarias mas ciclo real de deriva/revision. UML-004: reglas en AGENTS, SDD, perfiles y guia de mantenimiento por cambio.
Los hashes detectan solo entradas y referencias declaradas; no demuestran semantica ni ausencia de dependencias omitidas. El estado conserva semantic_review y visual_review REQUIRED por defecto; esta inspeccion de ejemplos se registra aqui, no como aprobacion de modelos de una aplicacion.
Los ejemplos sinteticos no documentan SITOP V2, Tribe Sport ni SPI Generator. Las evaluaciones de comportamiento de los agentes/skills siguen NOT_RUN; las pruebas tecnicas de render no las sustituyen. No se ha creado una automatizacion periodica ni actualizado dependencias a latest sin fijarlas.
