# Estándar de modelado UML

Estado inicial: alpha 0.1.0. Un modelo debe responder una pregunta concreta para una audiencia definida.

## Semántica y alcance

Declarar si el modelo representa análisis, diseño propuesto o implementación observada.
Mantener un vocabulario del dominio consistente con requisitos y otros modelos.
Elegir el tipo de diagrama por su propósito; no producir un catálogo de diagramas por defecto.
Expresar multiplicidades, composición, estados o fronteras únicamente con soporte en las entradas.
Usar notas para supuestos y decisiones abiertas sin presentarlos como hechos confirmados.
Separar nivel conceptual de detalles técnicos cuando mezclarlos dificulte la lectura.

## Trazabilidad

Asociar cada modelo al escenario, requisito o decisión que explica usando identificadores existentes.
Si representa código, indicar componentes o rutas verificadas y divergencias relevantes.
Mantener coherencia de nombres, operaciones, actores y responsabilidades entre diagramas.
Los diagramas complementan criterios de aceptación, contratos y ADR; no los sustituyen.

## Artefactos y revisión

Entregar fuente editable y revisar legibilidad: fronteras, etiquetas, dirección del flujo y densidad.
PlantUML es una opción de serialización; su sintaxis no demuestra por sí sola corrección UML.
Comprobar que el renderizador existe antes de ejecutar; distinguir revisión semántica de render técnico.
Una imagen sin su fuente editable requiere explicar la limitación cuando se pide mantenimiento.
No enviar modelos internos a servicios externos de render sin autorización para compartir sus datos.
Registrar qué fue comprobado y qué sigue supuesto o pendiente; no declarar render PASS sin ejecución.

## Herramientas y actualizacion continua por cambio

Usar PlantUML y Mermaid oficiales como fuentes editables comunitarias, sin copiar skills de procedencia incierta. [Guia de instalacion/render](../../docs/uml.md) y [toolchain fijada](../tools/uml-toolchain.json). PlantUML cubre los diagramas UML formales; Mermaid facilita los tipos que soporta en Markdown. Render valido no demuestra conformidad semantica con OMG UML.

Todo cambio de software evalua impacto en modelos: escenarios, API, clases/datos, colaboraciones, estados, componentes y despliegue. Actualizar los afectados antes del cierre; registrar razon de no afectacion cuando corresponda. Registrar fuente y referencias locales en diagrams.json, generar artefactos y verificar hashes con scripts/uml.py check. Un cambio en codigo sin cambio de fuente exige una nota explicita de revision al regenerar.
La vigencia automatica se limita a archivos declarados, herramientas y artefactos; no detecta por si sola una relacion incorrecta o un archivo relevante omitido. La revision visual/semantica es independiente y el estado no la declara aprobada. Fuentes y estado ligero se versionan; imagenes y runtimes locales no.
Revisar versiones de herramientas de forma deliberada, fijar y probar actualizaciones; no cambiar dependencias silenciosamente. No hay daemon ni tarea programada creada por esta regla.

## Fuentes

- [OMG: especificación UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/).
- [PlantUML: secuencias](https://plantuml.com/sequence-diagram).
- [PlantUML: clases](https://plantuml.com/class-diagram).
