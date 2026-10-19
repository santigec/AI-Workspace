# CodeGraph compartido para los proyectos

AI-Workspace proporciona la version fijada, launcher, configurador y reglas. Cada producto conserva codigo y un indice local propio. Es una herramienta complementaria a SDD/OpenSpec y Engram; no instala Gentle-AI ni crea perfiles de agentes especializados.

## Preparar este equipo u otro

Con acceso al repo, Node y Python 3.11+:

```powershell
cd [ruta-de-AI-Workspace]
npm ci
node scripts/codegraph.mjs --version
python scripts/configure_codegraph.py
```

El configurador registra el MCP en la configuracion de Codex de ese usuario y anade un bloque propio a sus instrucciones globales. Preserva otras configuraciones, guarda copia local de los archivos existentes y es idempotente. Si encuentra una entrada codegraph ajena al bloque administrado, se detiene para revisar la fusion; no la reemplaza silenciosamente. Si Node no esta en PATH usar `--node [ruta-absoluta-node]`. No versionar esa configuracion personal ni sus backups.
Comprueba paquete 1.6.2, desactiva telemetria, expone solo codegraph_explore y usa rutas absolutas locales. Tras la configuracion abrir una nueva sesion de Codex o recargar su conexion MCP y comprobar disponibilidad; una conversacion abierta puede conservar su inventario anterior. `codex mcp get codegraph` comprueba registro, no demuestra una llamada real desde el chat.

## Inicializar una aplicacion

Ejemplo con la ruta proporcionada por el usuario, **no ejecutado automaticamente sobre SPI Generator**:

```powershell
node F:\ai\workspace\AI-Workspace\scripts\codegraph.mjs init F:\ja3\spi-generator --yes
node F:\ai\workspace\AI-Workspace\scripts\codegraph.mjs status F:\ja3\spi-generator --json
node F:\ai\workspace\AI-Workspace\scripts\codegraph.mjs explore "[archivo o simbolo y pregunta]" --path F:\ja3\spi-generator --max-files 3
```

Antes de init, anadir `.codegraph/` y `.codegraph-*/` a las exclusiones del proyecto y revisar sus carpetas generadas/dependencias. No copiar el codigo a AI-Workspace. Para cambios no actualizados por watcher usar `sync [ruta-proyecto]` y revisar status. El watcher no equivale a sincronizacion entre equipos.

## Invocacion desde un proyecto

```text
Usa las reglas de AI-Workspace desde [ruta accesible y revision].
Para explorar este codigo aplica codegraph-navigation.
Consulta el indice de este proyecto con projectPath explicito
y maxFiles acotado. Si falta indice o MCP, indica la limitacion
y usa lectura dirigida. Mantiene SDD/OpenSpec y pruebas reales.
```

En el AGENTS.md del producto registrar la ruta accesible de AI-Workspace, commit utilizado y referencias a sus politicas SDD/CodeGraph. Revisar primero instrucciones existentes; mencionar el repo por nombre o enlazar su GitHub no concede acceso ni carga automaticamente skills/MCP.

| Componente | Que hace falta en cada proyecto/equipo |
|---|---|
| Reglas | Archivos accesibles e instrucciones del producto que las referencien |
| Skills propios | Lectura explicita por ruta o instalacion que conserve referencias; el nombre solo no instala |
| MCP CodeGraph | Configuracion local de Codex y sesion que lo cargue |
| Indice | init en la aplicacion; local e ignorado por Git |
| OpenSpec | Configuracion y artefactos del producto; no hereda automaticamente los de AI-Workspace |
| Engram | Consultar proyecto correcto e importar/exportar explicitamente |

## Comprobar instalacion y pruebas

```powershell
npm run test:codegraph
python -m unittest discover -s tests -p test_configure_codegraph.py
```

Las pruebas CodeGraph crean proyectos sinteticos locales bajo .tools; el caso sin indice se crea al lado del repo para no heredar su indice por busqueda de ancestros. Comprueban la conexion MCP y consultas de distintos lenguajes/indices, ademas de cambios tras sync. No equivalen a indexacion ni verificacion de aplicaciones reales, ni a medicion comparativa de tokens.

Para reducir contexto, consultar el flujo o simbolo relevante y reutilizar su fuente retornada. Las relaciones estaticas incompletas y resultados recortados requieren inspeccion adicional. [Politica completa](../software-office/standards/codegraph.md).
