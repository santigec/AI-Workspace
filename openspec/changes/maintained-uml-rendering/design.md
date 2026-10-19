## Context

La oficina mantiene SDD/OpenSpec, CodeGraph y herramientas locales. Hay un borrador de modelado UML que no se ha publicado y no se ha comprobado su renderizado. El usuario pide fuentes mantenibles y graficos profesionales, no solo texto.

## Goals / Non-Goals

Goals: render real, skills propios basados en herramientas comunitarias oficiales, modelos editables y deteccion de deriva. Non-goals: inventar arquitectura de aplicaciones no disponibles, garantizar semantica mediante hashes, sustituir aceptacion institucional o un daemon que regenere sin revision.

## Decisions

- PlantUML1.2026.9 descargado de Maven Central con SHA256 fijado; Mermaid CLI12.0.0 en lockfile npm. Usar Chrome local disponible para Mermaid sin descargar navegador adicional.
- Java8 instalado no ejecuta el JAR actual (requiere11+); usar runtime Temurin21 local fijado y verificado, sin cambiar JAVA_HOME o versiones de aplicaciones. Para ejemplos PlantUML usar layout smetana cuando corresponda, evitando dependencia obligatoria en Graphviz externo.
- Un manifiesto ligero por proyecto identifica fuente, engine y referencias de codigo. Estado de render almacena hashes de fuente, referencias, herramienta y artefactos locales; check rechaza deriva.
- Si cambian referencias de codigo y la fuente del diagrama sigue igual, render exige una nota explicita de revision. Esto evidencia la decision, no certifica su correccion. La revision semantica y visual sigue siendo necesaria.
- Generar SVG y PNG en outputs/uml; fuentes y manifiestos van a Git, imagenes y binarios quedan locales conforme a prioridad del usuario.
- Modelado formal usa PlantUML; Mermaid cubre los tipos que realmente soporta. No afirmar conformidad integral UML por aceptar sintaxis.

## Risks / Trade-offs

Un archivo referenciado puede cambiar sin afectar el modelo; se permite justificarlo en lugar de inventar cambios visuales. Los hashes no detectan cambios en codigo omitido del manifiesto, por lo que la seleccion de referencias requiere revision. Versiones fijadas necesitan mantenimiento deliberado; no hay promesa de actualizar paquetes automaticamente.

## Migration Plan

Instalar y probar aqui con ejemplos sinteticos. Al abrir cada aplicacion identificar modelos, referencias y tareas SDD pertinentes, conservando formatos existentes. No trasladar aplicaciones a este repo ni crear diagramas que afirmen estructura no inspeccionada.

## Open Questions

Rutas, diagramas y dependencias reales de cada aplicacion deben determinarse al adoptarlo; los ejemplos no son documentacion de esas aplicaciones.
