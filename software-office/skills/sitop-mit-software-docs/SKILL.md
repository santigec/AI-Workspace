---
name: sitop-mit-software-docs
description: Genera y mantiene documentación de software de la oficina SITOP del MIT, con análisis, diseño, trazabilidad F0-F5 e índices navegables en Word y Markdown. Usar para proyectos SITOP/MIT, conservando identidad, stack y fuentes de cada producto.
---

# Documentación de software SITOP / MIT

Fuente principal reutilizable de AI-Workspace; no depende de SPI Generator. Aplicar al proyecto solicitado de la oficina SITOP/MIT, sin imponer su identidad a otras oficinas. Para una corrección puntual actualizar solo los documentos afectados; no rehacer el expediente completo por rutina.

## Entradas y alcance

Identificar producto, repositorio, versión/caso, fuentes disponibles y documentos existentes. Inspeccionar código, scripts, configuración y pruebas antes de describir comportamiento. Separar hechos comprobados, observación estática, supuestos, decisiones pendientes y propuestas. Conservar cambios locales y configuración; documentar no autoriza corregir el programa.

Consultar [SDD/OpenSpec](../sdd-openspec/SKILL.md), [proceso institucional](../../standards/institutional-process.md) y [formularios](../../knowledge/institutional-forms.json) según el alcance. Las specs de aplicación permanecen en su repositorio. Usar CodeGraph si está disponible e indexado con ruta explícita del producto y consultas acotadas; las relaciones estáticas no prueban ejecución. No activar delegación por defecto.

## Expediente y trazabilidad

Leer [estructura y mantenimiento](references/dossier.md) para análisis, diseño, proceso e impacto. Conservar IDs estables RF/RNF, CU, SEQ y CP, y distinguir comportamiento observado de mejoras. Para el expediente completo, cada CU documentado tiene secuencia referenciada que explica sus interacciones. Diccionario de datos cuando exista modelo/archivo/contrato; indicar no aplicable con motivo cuando corresponda. Seguir [UML](../uml-modeling/SKILL.md) y [render local](../uml-rendering/SKILL.md), manteniendo fuente editable, referencias y revisión semántica.

## Formato MIT

Leer [perfil gráfico](references/office-profile.md) y [recursos y portabilidad](references/resources.md). Usar los membretes originales vertical/horizontal verificados, sin deformarlos. Portada con título/logos y sin número visible; segunda hoja muestra 2 de N. Desde esa hoja: control con producto/título, código, versión, creado/actualizado y elaborado/revisado/aprobado; pie gráfico y PAGE/NUMPAGES continuo, incluso al cambiar orientación. Historial por documento: versión, fecha, descripción y responsable real o pendiente.

El helper [sitop_mit_template.py](scripts/sitop_mit_template.py) prepara portada, controles y cambio de orientación. No genera el expediente ni el índice por sí solo. Agregar títulos nativos, TOC actualizable con páginas verificadas, marcadores y vínculos internos/entre documentos. Mantener Word editable y navegación Markdown. Código, personas, fechas de revisión y firmas no confirmados quedan pendientes. No heredar datos de ejemplos.

## Verificación y entrega

Usar el runtime/document tools disponible para DOCX, renderizar todas las páginas finales e inspeccionar tablas, diagramas, márgenes, logos, encabezados, pies y secciones. Comprobar enlaces, índices contra el render y continuidad PAGE. Si faltan membretes o render, entregar avance claramente identificado y declarar esa verificación pendiente; no reemplazar marca por logos inventados ni afirmar revisión visual.

Entregar rutas a documentos y fuentes, versión editorial y evidencia de comprobaciones. Registrar status PASS/FAIL/SKIPPED/NOT_RUN por verificación, evidence, warnings, missing_inputs, next_skill y artifact según el contrato del workspace. La revisión/aprobación institucional permanece separada. Un render, TOC o OpenSpec válido no prueba la aplicación. Registrar cómo regenerar y cuál es la siguiente prueba funcional real.

Conservar en Git reglas, catálogos, Markdown, fuentes UML y evidencia ligera. DOCX/PPTX/PNG/PDF, runtimes y originales MIT quedan locales; no procesar datos operativos para fixtures. Reincorporar ediciones aceptadas de Word a las fuentes antes de regenerar.
