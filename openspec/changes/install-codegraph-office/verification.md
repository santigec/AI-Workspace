# Verificacion de CodeGraph para las oficinas

Fecha: 2026-10-19. Candidato: base 0af0703 mas el diff acotado CodeGraph. Windows con Node v24.19.0 como launcher y paquete @colbymchenry/codegraph 1.6.2 con runtime propio. No se realizaron pruebas de aplicaciones productivas ni comparativa de tokens.

## Instalacion y configuracion reales

- Paquete y plataforma instalados localmente con npm, version CLI 1.6.2 comprobada y lockfile conservado.
- `node scripts/codegraph.mjs init . --yes` creo el indice de AI-Workspace. Tras sync: 36 archivos, 269 nodos y 444 relaciones; pendingChanges cero en esa comprobacion. Son estadisticas de exploracion, no cobertura de pruebas.
- Configurador aplicado al Codex local, con backup en el directorio de usuario y sin modificar otras entradas MCP. Segunda ejecucion devolvio unchanged.
- `codex mcp get codegraph --json` reconoce el registro STDIO, launcher local y enabled_tools limitado a codegraph_explore. Telemetria desactivada comprobada con `telemetry status`.
- `.codegraph/` y variante WSL excluidas comprobadas mediante git check-ignore. No se incorporan indices, binarios o node_modules al commit.

## Pruebas ejecutadas

| Alcance | Comando | Resultado |
|---|---|---|
| Version/lock, handshake y tools/list, Python/Java/TypeScript, dos proyectos con simbolos iguales, indice ausente, sync | `node --test tests/test_codegraph.mjs` | PASS: 6 |
| Preservacion de config/backups, idempotencia, conflicto ajeno, marcadores invalidos y version incorrecta | `python -m unittest discover -s tests -p test_configure_codegraph.py` | PASS: 5 |
| Regresion Python incluido configurador | `python -m unittest discover -s tests` en copia del alcance publicable | PASS: 48, incluye los 5 anteriores |
| Regresion OpenSpec y perfiles actualizados | `node --test tests/test_openspec.mjs` | PASS: 6 |
| Registro y referencias del alcance publicable | `python scripts/validate_workspace.py` en la misma copia | PASS |
| Specs/cambio propios | `openspec validate --all --strict --no-interactive` | PASS |

Las pruebas MCP usaron un cliente JSON-RPC real con initialize, tools/list y tools/call frente al servidor instalado, no un mock del protocolo. Se limitaron a codigo sintetico y servidores sin watcher/daemon en los tests. La suite Python se ejecuto sobre archivos controlados por Git y el diff seleccionado, excluyendo los 18 borradores anteriores sin registrar. En el checkout principal esos 18 siguen pendientes; no se atribuye a esta entrega haberlos integrado.

## Trazabilidad

CG-001: package.json/lock, launcher y prueba de version. CG-002: politica de proyecto explicito, indices locales y pruebas de aislamiento/sync. CG-003: configurador, preservacion de ajustes y protocolo real con una sola herramienta expuesta. CG-004: guia, politica, instrucciones y distincion entre ahorro esperado y medido. SDD-001: exploracion previa ligada a CodeGraph en skill, workflow y perfiles.

## Hallazgos y limites

La primera prueba de indice ausente estaba debajo de un ancestro indexado: el servidor resolvio ese ancestro y devolvio una busqueda sin coincidencias. Se movio el caso a una carpeta sin ancestro indexado y se verifico la orientacion de inicializacion. Se documenta comprobar raiz resuelta, no suponer aislamiento por nombre de subcarpeta.
El grafo inicial dijo no encontrar enlaces a ciertos tests aunque existian y se ejecutaban 43 pruebas Python. No interpretar ausencia de enlaces como ausencia de pruebas ni reemplazar verificacion dinamica por grafo.
La sesion de chat actual no expone aun herramientas CodeGraph en su inventario, aunque el servidor se verifico con el cliente de prueba. Abrir una sesion que cargue el nuevo MCP antes de afirmar acceso nativo desde el chat.
SPI Generator, SITOP V2 y Tribe Sport no se han inicializado ni indexado en esta entrega. Las evaluaciones de comportamiento de codegraph-navigation siguen NOT_RUN. No hay porcentaje medido de ahorro de tokens ni autorizacion de produccion inferida.
