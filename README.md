# AI Workspace

Repositorio central para capacidades de IA reutilizables. Versión inicial: **0.1.0**.

## Áreas

- **shared/**: skills, conocimiento, plantillas y estándares comunes.
- **tribe/**: productos, sublimación y DTF.
- **image-studio/**: análisis, generación, edición y preparación de imágenes.
- **software-office/**: SQL, diseño de sistemas y comunicación técnica.
- **experiments/**: pruebas antes de promover una capacidad a estable.

## Separación de responsabilidades

**Skill** describe cómo hacer algo; **knowledge** contiene datos y reglas del dominio; **template** define la forma del resultado; **tool** ejecuta una operación. Las carpetas de agentes quedan reservadas para una fase futura.

Las capacidades comunes pertenecen a shared. La lógica del negocio pertenece a su dominio. image-analysis vive en shared para que Image Studio y Tribe puedan reutilizarlo sin duplicarlo.

## Uso

1. Selecciona el SKILL.md correspondiente a la solicitud.
2. Consulta sus referencias y las especificaciones del producto, cuando aplique.
3. Ejecuta con las herramientas disponibles en tu entorno.
4. Revisa el resultado y registra limitaciones.

Este repositorio almacena las fuentes; no instala automáticamente skills ni conecta modelos o herramientas.

## Primer flujo: arte para impresión

Solicitud + imagen → shared/skills/image-analysis → skill de Image Studio → tribe/skills/product-specs → image-studio/skills/print-ready-qa.

Usa [la ficha de producto](tribe/templates/product-spec.md). Confirma dimensiones, técnica, resolución, fondo y márgenes antes de producir el archivo final.

## Desarrollo

Editar → probar con un caso real → revisar → commit → GitHub → instalar la versión estable en el entorno elegido.

Lee [la guía de skills](shared/standards/skill-writing-guide.md) y [las reglas de calidad](shared/standards/quality-rules.md).
Los 16 skills de esta versión son una base inicial; la validación estructural no sustituye pruebas con productos y archivos reales.
