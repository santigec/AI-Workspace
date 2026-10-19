---
name: uml-modeling
description: Crea y revisa modelos UML editables y trazables a requisitos, decisiones y código para análisis o diseño de software.
---

# Modelado UML

## Alcance y entradas

Aplicar cuando un modelo ayude a explicar dominio, interacción, estructura o estados.
Recibir audiencia, propósito, requisitos y código disponible. Diferenciar análisis del negocio,
diseño propuesto y estructura observada; no presentar una propuesta como sistema implementado.
Seguir [SDD/OpenSpec](../../standards/sdd-openspec.md) y el [estándar UML](../../standards/uml.md).
SITOP V2 conserva trazabilidad y formularios institucionales; Tribe Sport usa documentacion mas ligera sin perder escenarios ni evidencia.

## Acciones

1. Identificar la pregunta del modelo, actores, frontera y escenarios. Separar hechos,
   supuestos y decisiones pendientes; asignar referencias de requisitos cuando existan.
2. Elegir el diagrama que resuelva la pregunta: casos de uso para objetivos, clases para
   conceptos/relaciones, secuencia para colaboración, actividad para decisiones y flujo,
   estados para ciclo de vida, componentes o despliegue para estructura pertinente.
3. Modelar primero el recorrido importante y sus alternativas relevantes. Evitar generar
   todos los tipos de diagrama o replicar cada clase del código sin necesidad.
4. Usar nombres del dominio consistentes; precisar multiplicidades y composición solo
   cuando se conozca su semántica. No convertir tablas de datos automáticamente en dominio.
5. Para secuencias, mostrar mensajes, responsables, respuestas relevantes, condiciones y
   errores; conservar coherencia con operaciones y responsabilidades del diseño.
6. Entregar fuente editable .puml o Mermaid para tipos realmente soportados. Aplicar
   [uml-rendering](../uml-rendering/SKILL.md) para generar e inspeccionar graficos locales;
   no suponer herramientas instaladas en otro equipo ni llamar UML formal a cualquier flowchart.
7. Revisar consistencia entre diagramas, requisitos y código. Registrar trazabilidad suficiente
   para ubicar qué escenario o decisión representa cada modelo y detectar divergencias.
8. Si hay render disponible y autorizado, generar e inspeccionar la vista; corregir legibilidad
   y etiquetas. Si no, revisar el texto y declarar render/sintaxis no ejecutados según corresponda.
9. Al cambiar escenarios, contratos, clases, estados o despliegue, revisar los modelos afectados
   en la misma entrega. Mantener manifiesto de fuentes/referencias y ejecutar check de vigencia;
   justificar cambios de codigo que no requieren alterar el modelo. Los hashes no prueban semantica.

## Evidencia de salida

- Diagrama, propósito y fuente editable; referencias de requisitos/código/ADR pertinentes.
- Supuestos, decisiones abiertas y diferencias entre diseño y sistema observado.
- Revisión semántica y estado explícito del render; imagen opcional cuando se haya verificado.

## Límites

No inferir infraestructura, escala, servicios ni cardinalidades no respaldadas por entradas.
No usar diagramas como sustituto de contratos, criterios de aceptación o decisiones explicadas.
No enviar modelos con información interna a un renderizador externo sin autorización para ello.

## Referencias

[Catálogo de fuentes](../../knowledge/engineering-sources.md).
- [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/).
- [PlantUML: secuencias](https://plantuml.com/sequence-diagram).
- [PlantUML: clases](https://plantuml.com/class-diagram).
