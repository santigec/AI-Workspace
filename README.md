# AI Workspace

Repositorio central para capacidades de IA reutilizables. Versión de desarrollo: **0.2.0 — Evaluation foundation**.

## Áreas

- **shared/**: skills, conocimiento, plantillas y estándares comunes.
- **tribe/**: productos, sublimación y DTF.
- **image-studio/**: análisis, generación, edición y preparación de imágenes.
- **software-office/**: SQL, diseño de sistemas y comunicación técnica.
- **experiments/**: pruebas antes de promover una capacidad a estable.
- **evals/**: 12 escenarios de evaluación y plantilla de evidencia.
- **registry/**: versiones, propietarios, estados y dependencias de los 16 skills.
- **workflows/**: sublimación, edición de imagen y diseño de sistemas.
- **standards/**: contratos y evaluación; los estándares generales siguen en shared/standards.

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
Los 16 skills conservan estado alpha. image-analysis, sublimation-layout y print-ready-qa tienen contratos de entrada, salida y terminación en versión 0.2.0. Los otros skills siguen en 0.1.0.

Consulta [el registro](registry/skills.yaml), [los contratos](standards/skill-contract.md) y [la guía de evaluación](standards/evaluation-guide.md).

Desde la raíz del repositorio, con Python 3.10 o posterior:

```console
python scripts/validate_workspace.py
python -m unittest discover -s tests
```

Estos controles validan estructura y consistencia. Los 12 casos de comportamiento están NOT_RUN; no se han usado imágenes reales ni aprobado productos para producción.
develop contiene la base v0.2; main mantiene la última versión publicada. El siguiente paso es ejecutar los casos con archivos y especificaciones reales, guardar evidencia y corregir los skills antes de promoverlos.
