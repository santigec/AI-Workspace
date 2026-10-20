# Documentación de software SITOP / MIT

La fuente principal es [sitop-mit-software-docs](../software-office/skills/sitop-mit-software-docs/SKILL.md), versión 0.1.0 alpha. Sirve para otros productos de la oficina, conservando su nombre, stack y fuentes. No depende de rutas, catálogo o código de SPI Generator.

Invocación en AI-Workspace: `$sitop-mit-software-docs documenta este proyecto para la oficina de software SITOP del MIT`. Desde otro repositorio, indicar la ruta del checkout de AI-Workspace y leer la skill central. No se promete descubrimiento automático en otros proyectos/equipos.

Incluye reglas de análisis, diseño, proceso, requisitos RF/RNF, casos de uso/secuencias, diccionario pertinente, matriz de impacto y pruebas relacionadas con F0-F5. DOCX con portada/logos sin numeración visible, control de cambios, encabezado/pie y numeración continua desde segunda hoja, títulos e índices navegables. Los responsables y las firmas se completan con datos confirmados. Mantener fuentes editables y revisión visual final.

[Recursos y traslado a otro equipo](../software-office/skills/sitop-mit-software-docs/references/resources.md): Git lleva conocimiento ligero y helper; originales MIT en .tools/sitop-mit permanecen locales. No se publica la skill pública de terceros ni los binarios privados. El caso SPI 0.3 fue revisado en 29 páginas; esta evidencia apoya el perfil, no demuestra evaluación de un segundo proyecto. Nueva generación/render y aceptación institucional se comprueban por entrega.

Estado de integración: verificación estructural y publicación se registran al cierre; evaluación de ejecución de la skill en segundo producto NOT_RUN. Sin cambios semánticos de software o UML: esta integración distribuye reglas y helper de maquetación existente.

## Verificación de integración — 2026-10-20

PASS: validate_workspace.py (registro, estructura, enlaces y workflows), quick_validate.py del creador de skills, OpenSpec estricto (cinco elementos antes de archivo), SHA256 de dos membretes locales y helper idéntico al ya probado. Smoke sintético OOXML: portada sin PAGE, controles y segunda sección horizontal sin reinicio PASS. No se cambió el helper, por lo que no se repitió la revisión visual anterior de su perfil; render de este smoke NOT_RUN. Evaluación integral de la nueva skill en segundo producto NOT_RUN. Registro: 45 skills (28 alpha, 17 experimental).

Los membretes privados están ignorados en .tools; no se suben Word/PPTX ni herramientas. La publicación se verifica contra origin/develop tras el push.
