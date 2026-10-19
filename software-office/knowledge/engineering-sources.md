# Fuentes de ingenieria — modelado y diagramas

Revisadas el 2026-10-19. Las instrucciones del workspace son adaptaciones propias para sus oficinas, no copias de skills comunitarios ni certificaciones. Se eligieron herramientas de codigo abierto mantenidas publicamente, con documentacion y repositorios oficiales; no se afirma que sean objetivamente las mejores para todo uso.

- [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1/): referencia de semantica de modelado; aceptar un archivo PlantUML no certifica cumplimiento completo.
- [PlantUML](https://github.com/plantuml/plantuml), [CLI](https://plantuml.com/command-line), [Smetana](https://plantuml.com/smetana02): fuentes textuales para UML y render local; comprobar opciones en la version fijada.
- [Mermaid](https://github.com/mermaid-js/mermaid), [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli), [clases](https://mermaid.js.org/syntax/classDiagram), [secuencia](https://mermaid.js.org/syntax/sequenceDiagram): diagramas editables adecuados a documentacion y a sus tipos soportados; no inventar soporte de casos de uso formales.
- [Eclipse Adoptium](https://adoptium.net/temurin/): runtime Java local para las herramientas cuando el Java de aplicaciones es incompatible; no alterar el toolchain de proyectos por instalar el renderizador.

Versiones y checksums en software-office/tools/uml-toolchain.json; versiones npm fijadas en package-lock.json. Consultar fuentes oficiales al actualizar y ejecutar nuevamente render, controles e inspeccion; no copiar pins de ejemplos antiguos sin comprobar compatibilidad.
