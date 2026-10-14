# AI Workspace

Repositorio central para capacidades de IA reutilizables. Versión de desarrollo: **0.2.1 — Tribe orders foundation**.

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
Los 16 skills conservan estado alpha. image-analysis, sublimation-layout y print-ready-qa tienen contratos en versión 0.2.0; product-specs integra el catálogo en 0.2.1. El registro indica la versión de cada skill.

Consulta [el registro](registry/skills.yaml), [los contratos](standards/skill-contract.md) y [la guía de evaluación](standards/evaluation-guide.md).

Desde la raíz del repositorio, con Python 3.10 o posterior:

```console
python scripts/validate_workspace.py
python -m unittest discover -s tests
```

Estos controles validan estructura y consistencia. Los 12 casos de comportamiento están NOT_RUN; no se han usado imágenes reales ni aprobado productos para producción.
develop contiene la base v0.2; main mantiene la última versión publicada. El siguiente paso es ejecutar los casos con archivos y especificaciones reales, guardar evidencia y corregir los skills antes de promoverlos.

## Pedidos de Tribe

AI-Workspace almacena conocimiento, skills y reglas. Un pedido es una ejecución que consume esa base; no necesita otro repositorio por diseño.
Los pedidos reales, outputs y logs pertenecen a un futuro design-runner separado. Este repositorio contiene solo ejemplos sintéticos; todavía no ejecuta pedidos ni genera arte por sí mismo.

- [Catálogo de productos](tribe/knowledge/product-catalog/README.md): cuatro variantes con medidas propuestas y tres familias pendientes.
- [Schema de pedidos](tribe/schemas/README.md): producto, workflow, contenido, salida, restricciones hard/soft y referencia al commit.
- [Principios de diseño](tribe/standards/design-principles.md) y [generación no bloqueante](tribe/policies/non-blocking-generation.md).
- Workflows: [taza](workflows/tribe/mug-sublimation.md), [tomatodo](workflows/tribe/tumbler-sublimation.md) y [camiseta DTF](workflows/tribe/dtf-shirt.md).

Invocación manual: "Usa tumbler-sublimation con tumbler_600ml, modo draft, esta temática y las restricciones del pedido".
Todos los productos están unverified. La resiliencia permite un borrador claramente identificado; no relaja restricciones hard ni certifica impresión.

Para validar catálogo y pedidos, instala jsonschema (probado con 4.26.0):

```console
python -m pip install -r requirements-dev.txt
python scripts/validate_order.py
python scripts/validate_order.py tribe/templates/orders/tumbler-draft.example.json
python -m unittest discover -s tests
```

INPUT_READY valida entradas. PRINT_READY exige un archivo realmente generado y QA posterior.
