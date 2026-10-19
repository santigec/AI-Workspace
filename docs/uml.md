# UML editable, graficado y actualizado

Las oficinas usan dos skills propios: **uml-modeling** para semantica y trazabilidad y **uml-rendering** para graficos, inspeccion y vigencia. Se apoyan en herramientas comunitarias oficiales: PlantUML para UML formal y Mermaid para tipos adecuados a documentacion. No se han copiado skills de terceros ni se afirma un ranking universal.

## Instalar en cada equipo

Con Node >=22.13.0 para Mermaid CLI12, npm y Python3.11+:

```powershell
cd [ruta-AI-Workspace]
npm ci
python scripts/uml.py setup
```

Versiones fijadas: PlantUML1.2026.9, Mermaid CLI12.0.0 y runtime Temurin local para Windows x64. Setup verifica SHA256 del JAR y del ZIP descargados. Java predeterminado de esta PC era8 y no sirve para ese JAR; la herramienta utiliza su JRE local21 sin cambiar JAVA_HOME ni Java de aplicaciones. En otros sistemas o arquitecturas usar `--java [java-compatible]` con Java11+.
Mermaid usa Chrome/Chromium local; si no se detecta, pasar `--browser [ruta]` a render. No se descarga ni se requiere un navegador en Git. Herramientas, runtime y configuracion de navegador quedan en carpetas locales ignoradas.

## Probar los modelos de ejemplo

```powershell
python scripts/uml.py render --manifest software-office/templates/uml/diagrams.example.json
python scripts/uml.py check --manifest software-office/templates/uml/diagrams.example.json
```

Genera diez modelos en SVG y PNG bajo outputs/uml: siete PlantUML (casos de uso, clases, secuencia, actividad, estados, componentes y despliegue) y tres Mermaid (clases, secuencia, estados). Son ejemplos, no la arquitectura de SITOP, Tribe Sport ni SPI.
El render se ejecuta localmente y los ejemplos PlantUML usan Smetana donde corresponde para no exigir Graphviz externo. Los modelos de otros proyectos pueden requerir otro layout o dependencias: comprobarlo antes de prometer render equivalente.

## Mantener modelos de una aplicacion

Crear un inventario `docs/uml/diagrams.json` en la aplicacion, por ejemplo:

```json
{
  "schema_version": 1,
  "diagrams": [
    {
      "id": "consulta-pedido",
      "engine": "plantuml",
      "scope": "observed",
      "source": "docs/uml/consulta-pedido.puml",
      "code_refs": ["src/ruta-real-del-servicio.java"]
    }
  ]
}
```

Usar archivos reales y pertinentes. scope es example, proposed u observed; este ultimo exige referencias de codigo inspeccionadas. No trasladar el codigo al workspace. Desde cualquier proyecto ejecutar el script central con `--project [ruta-aplicacion]` y su manifiesto relativo. Se puede seleccionar `--diagram [id]` para renderizar una pieza.

Conservar fuente, inventario y archivo `.render-state.json` ligero en Git. Las imagenes van a outputs/uml y quedan fuera de Git segun las reglas de esta oficina. En una maquina nueva hay que renderizar para recuperar esas imagenes locales antes de check.

## Regla de actualizacion en cada cambio

1. Analizar con requisitos/codigo y CodeGraph cuando aporte contexto que modelos afecta el cambio.
2. Actualizar fuente UML, referencias y tareas SDD correspondientes.
3. Renderizar y ejecutar check; abrir graficos y revisar semantica, nombres, flechas, cardinalidades y legibilidad.
4. Si el codigo cambio pero el modelo sigue siendo correcto sin alterarlo, revisarlo y usar `--review-note "razon concreta de por que el cambio no altera el modelo"` al renderizar. Esa nota documenta una decision, no certifica su verdad.
5. Registrar evidencias y pendientes antes de completar la tarea. Si ningun modelo aplica, explicarlo en el cambio; no generar UML sin proposito.

Check compara hashes de fuente, referencias declaradas, toolchain y artefactos generados. Detecta deriva, no errores semanticos ni archivos omitidos del inventario. CURRENT_HASHES no significa aprobacion UML. El estado deja revision visual/semantica como REQUIRED; documentar su resultado real en el informe del cambio.

Para CI o revision local ejecutar render/check y las pruebas del proyecto. No se ha instalado un workflow CI de una aplicacion no disponible ni un servicio automatico que modifique diagramas en segundo plano.

## Actualizar herramientas

Mantener diagramas actualizados con el codigo es obligatorio por cambio. Actualizar paquetes es una operacion distinta: consultar versiones oficiales al planificar mantenimiento o ante incompatibilidad, revisar cambios/licencias, modificar pins/checksums y lockfile, repetir pruebas y revisar graficos. No instalar latest silenciosamente ni crear una automatizacion periodica sin peticion de horario/frecuencia.

Fuentes: [estandar UML](../software-office/standards/uml.md), [catalogo de fuentes](../software-office/knowledge/engineering-sources.md), [PlantUML](https://github.com/plantuml/plantuml), [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli).
