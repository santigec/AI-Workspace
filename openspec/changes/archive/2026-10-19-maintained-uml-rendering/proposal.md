## Why

El usuario solicita skills para graficar UML con herramientas aceptadas por la comunidad y mantener los modelos actualizados. Existia un borrador local de uml-modeling sin integrar ni renderizador comprobado.

## What Changes

- Integrar uml-modeling y un skill uml-rendering con PlantUML y Mermaid oficiales, sin copiar skills comunitarios opacos.
- Instalar herramientas locales fijadas, renderizar SVG/PNG y revisar muestras reales.
- Mantener fuentes editables, referencias al codigo y comprobacion de deriva mediante hashes; exigir revision cuando cambie codigo referenciado.
- Integrar la actualizacion de UML al flujo SDD y controles de cada entrega, sin un servicio en segundo plano ni actualizaciones silenciosas de dependencias.

## Capabilities

### New Capabilities
- `maintained-uml`: Diagramas editables renderizables y control de vigencia respecto de sus fuentes y codigo.

### Modified Capabilities

Ninguna modificacion normativa a capacidades previas; los workflows SDD consumen esta capacidad adicional cuando el cambio afecta modelos.

## Impact

Dos skills de software, herramientas locales, modelos de ejemplo, documentacion y pruebas. Las imagenes generadas, navegador y JAR quedan fuera de Git. El JRE existente se comprueba sin cambiar toolchains de aplicaciones. No se modifica SPI, SITOP V2 ni Tribe Sport en esta entrega.
