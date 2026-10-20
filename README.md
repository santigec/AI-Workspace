# AI Workspace

[Codificacion local opcional](docs/local-coding.md): Qwen en LM Studio puede preparar propuestas de codigo en equipos habilitados. Codex conserva analisis, diseno, revision y pruebas; sin IA local continua con Codex. Configuracion y modelos quedan fuera de Git.

[UML editable y actualizado](docs/uml.md): skills uml-modeling y uml-rendering, PlantUML/Mermaid locales, graficos SVG/PNG y comprobacion de deriva contra codigo referenciado. Los modelos se revisan con cada cambio de software; las imagenes generadas permanecen locales.

[CodeGraph para las oficinas de software](docs/codegraph.md): herramienta local 1.6.2, configuracion reproducible para Codex e indices propios por proyecto fuera de Git. [Skill de navegacion](software-office/skills/codegraph-navigation/SKILL.md). Consultas acotadas para reducir lecturas repetidas; ahorro de tokens aun sin medicion comparativa.

Desarrollo de software: **SDD con OpenSpec** para SITOP V2 y Tribe Sport. [Guia de adopcion y continuidad](docs/sdd-openspec.md), [politica comun](software-office/standards/sdd-openspec.md) y [skill sdd-openspec](software-office/skills/sdd-openspec/SKILL.md). OpenSpec local 1.14.3; cada aplicacion mantiene sus propias especificaciones. Los perfiles especializados de agentes y la integracion de los otros skills de software siguen pendientes.

Cajas de taza: [mug-box-design](tribe/skills/mug-box-design/SKILL.md), arte plano y continuo **150 × 200 mm**, centro inferior libre, artes inferiores laterales, tema principal a 120 mm desde la base y borde temático. [Invocación y workflow](workflows/tribe/mug-box-design.md). Skill alpha 0.1.0; evaluaciones visuales pendientes.

Adhesivos para tarritos cuadrados: [adhesivo-tarrito](tribe/skills/adhesivo-tarrito/SKILL.md), banda plana y continua de **180 × 80 mm** para cuatro caras de 45 × 80 mm, con un foco centrado por panel y contenido crítico fuera de las uniones. [Workflow](workflows/tribe/adhesivo-tarrito.md). Skill alpha 0.1.0; evaluaciones visuales pendientes.

Tomatodo 750 ml: [tumbler-750ml-sublimation](tribe/skills/tumbler-750ml-sublimation/SKILL.md), **232 × 182 mm**, arte plano y continuo. [Ejemplo de orden](tribe/templates/orders/tumbler-750ml.example.json).

Repositorio central para capacidades de IA reutilizables. Versión de desarrollo: **0.5.6 — Documentación de software SITOP/MIT**.

Para usar dos equipos con GitHub: [guía de configuración y sincronización](docs/two-computers.md). Leer [estado para continuar](continuity/STATE.md). Se sincronizan skills y memoria `.engram` del proyecto `ai-workspace`; diseños y archivos pesados quedan locales.

[Equipo operativo](docs/operating-team.md): coordinador, diseñador y revisor. Tres perfiles de agente para pedidos de Tribe, con entrega y revisión independientes. El registro común contiene 45 skills: 28 alpha y 17 borradores experimentales de software preservados. [Pendientes y límites](continuity/PENDING.md).

## Áreas

- **shared/**: skills, conocimiento, plantillas y estándares comunes.
- **tribe/**: productos, sublimación y DTF.
- **image-studio/**: análisis, generación, edición y preparación de imágenes.
- **software-office/**: SQL, diseño de sistemas, comunicación técnica y SDD con OpenSpec; ampliacion especializada en preparacion.
- **experiments/**: pruebas antes de promover una capacidad a estable.
- **evals/**: 12 escenarios visuales/técnicos pendientes y una prueba lógica real ejecutada.
- **registry/**: versiones, propietarios, estados y dependencias de los skills registrados.
- **workflows/**: sublimación, edición de imagen y diseño de sistemas.
- **standards/**: contratos y evaluación; los estándares generales siguen en shared/standards.

## Separación de responsabilidades

**Skill** describe cómo hacer algo; **knowledge** contiene datos y reglas del dominio; **template** define la forma del resultado; **tool** ejecuta una operación. Los perfiles de agentes de Tribe viven en .codex/agents; los de las oficinas de software siguen pendientes.

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
Los 28 skills activos conservan estado alpha; los 17 borradores de software se registran como experimental 0.0.1, sin afirmar evaluación de comportamiento. image-analysis, sublimation-layout y print-ready-qa tienen contratos en versión 0.2.0; product-specs integra el catálogo en 0.2.1. mug-sublimation 0.1.2 y adhesivo-tarrito 0.1.0 son entradas desde chat. El registro indica la versión de cada skill.

Consulta [el registro](registry/skills.yaml), [los contratos](standards/skill-contract.md) y [la guía de evaluación](standards/evaluation-guide.md).

Desde la raíz del repositorio, con Python 3.10 o posterior:

```console
python scripts/validate_workspace.py
python -m unittest discover -s tests
```

Estos controles validan estructura y consistencia. Los 12 casos originales de comportamiento están NOT_RUN; una [prueba lógica real de pedido](evals/tribe/mug-sublimation/result-001.md) pasó la validación de entrada. No se ha generado arte ni aprobado un producto para producción.
develop contiene la base v0.2; main mantiene la última versión publicada. El siguiente paso es ejecutar los casos con archivos y especificaciones reales, guardar evidencia y corregir los skills antes de promoverlos.

## Pedidos de Tribe

AI-Workspace almacena conocimiento, skills y reglas. Un pedido es una ejecución que consume esa base; no necesita otro repositorio por diseño.
Los pedidos reales, outputs y logs pertenecen a un futuro design-runner separado. Este repositorio contiene solo ejemplos sintéticos; todavía no ejecuta pedidos ni genera arte por sí mismo.

- [Catálogo de productos](tribe/knowledge/product-catalog/README.md): taza, tres tomatodos, adhesivo para tarrito cuadrado y familias pendientes; todos conservan su estado de verificación explícito.
- [Schema de pedidos](tribe/schemas/README.md): producto, workflow, contenido, salida, restricciones hard/soft y referencia al commit.
- [Principios de diseño](tribe/standards/design-principles.md) y [generación no bloqueante](tribe/policies/non-blocking-generation.md).
- Workflows: [taza](workflows/tribe/mug-sublimation.md), [tomatodo](workflows/tribe/tumbler-sublimation.md), [adhesivo para tarrito](workflows/tribe/adhesivo-tarrito.md) y [camiseta DTF](workflows/tribe/dtf-shirt.md).

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

## Invocar el diseño desde otro chat

Consulta [prompts y acceso](docs/chat-invocation.md). El skill de entrada mug-sublimation está en .agents/skills para descubrimiento de Codex dentro de este checkout; su definición de dominio está en tribe/skills.
La entrada permite imágenes opcionales y fondo transparente, sólido o temático. El fondo no cambia las dimensiones del lienzo.
Ejemplo: "Usa mug-sublimation: taza 205 × 95 mm para Sebastián, dinosaurios infantiles, fondo temático como el adjunto. Genera y muestra PNG plano y continuo".


## Tomatodo de 500 ml

Usa [tumbler-sublimation](tribe/skills/tumbler-sublimation/SKILL.md): lienzo confirmado por el usuario de **232 mm de ancho × 125 mm de alto**, arte plano y continuo para impresión y sublimación.
Las reglas de taza se reutilizan con una composición propia para la proporción 232:125; no se estira el diseño de 205 × 95 mm.
Referencias opcionales, texto solicitado y fondo blanco, transparente o temático forman parte del pedido. Consulta [el ejemplo](tribe/templates/orders/tumbler-500ml.example.json).
Las dimensiones del lienzo están definidas para este flujo; el catálogo sigue sin aprobación completa de producción. Los dos nuevos casos visuales están NOT_RUN.


## Entrada específica: tomatodo 600 ml

[tumbler-600ml-sublimation](tribe/skills/tumbler-600ml-sublimation/SKILL.md) selecciona **232 × 142 mm**, plano y continuo.
Usa el workflow común tumbler-sublimation con product.id tumbler_600ml. La entrada específica no cambia el formato de la orden; evita confundir su altura con 125 mm de 500 ml.
Invoca con $tumbler-600ml-sublimation en Codex con el repositorio accesible. [Ejemplo de orden](tribe/templates/orders/tumbler-600ml.example.json).


## Agendas temáticas

[agenda-design](tribe/skills/agenda-design/SKILL.md) crea el conjunto de nueve modelos A4 vertical (210 × 297 mm) y dos etiquetas (205 × 165 y 205 × 95 mm).
Portadas y reversos mantienen la identidad; datos, calendarios, actividades y cuadrícula tienen base blanca, cabeceras/pies temáticos y escritura legible. La cuadrícula incorpora marca de agua central tenue.
Los años se resuelven desde la fecha del usuario; el ejemplo usa 2026 y 2027. Los calendarios se calculan, no se confían a texto dibujado por el modelo de imágenes.

Planificar y comprobar fechas, sin generar imágenes:

```console
python scripts/build_agenda_plan.py tribe/templates/orders/agenda-a4.example.json --out outputs/agenda-plan.json
```

El plan no es arte final ni aprobación de impresión. Los dos casos visuales de agenda están NOT_RUN.


Documentación de software SITOP/MIT: [skill reutilizable 0.1.0](software-office/skills/sitop-mit-software-docs/SKILL.md), [uso y portabilidad](docs/sitop-mit-software-docs.md). Análisis, diseño y trazabilidad con membretes, controles e índices. [Lista de skills y versiones](docs/skills-inventory.md).
