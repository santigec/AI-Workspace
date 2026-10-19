# CodeGraph en las oficinas de software

Aplicar a proyectos de software que consumen las reglas de AI-Workspace: SITOP V2, Tribe Sport y otros que las adopten. Herramienta elegida: **@colbymchenry/codegraph 1.6.2**, de colbymchenry/codegraph, tambien integrada por Gentle-AI. No instalar otras herramientas homonimas ni Gentle-AI por inferencia.

## Uso para contexto acotado

Para ubicar simbolos, relaciones, llamadas o impacto estatico, usar CodeGraph cuando el proyecto ya este indexado y la herramienta disponible. Indicar siempre `projectPath` absoluto de la aplicacion correcta. Empezar con una consulta especifica (archivo, simbolo y pregunta) y `maxFiles` reducido: 1 para un archivo conocido, 3-5 para un flujo. Ampliar solo si falta contexto.
Reutilizar el codigo actual que el resultado ya incluye; no abrir de nuevo todos los archivos por rutina. Leer los fragmentos omitidos, limites necesarios para editar, evidencia contradictoria o archivos marcados como cambiados desde el indice. Las busquedas textuales exactas, configuracion y formatos no cubiertos pueden resolverse mejor con rg y lecturas dirigidas. No usar el grafo para recuperar toda la documentacion Markdown de este workspace.
El limite maxFiles limita archivos, no garantiza un numero fijo de tokens ni que todos los simbolos retornados esten completos. Si el resultado se recorta, pedir el simbolo o archivo preciso. Medir llamadas y tokens comparables si se quiere cuantificar ahorro; no anunciar porcentajes tomados de publicidad o estimaciones sin ejecutar.

## Indice y limites de evidencia

Cada proyecto tiene su propio `.codegraph/`, con base SQLite y estado local. Comprobar inicializacion, proyecto, pendientes y avisos antes de confiar en relaciones relevantes. El watcher funciona cuando el servidor del proyecto esta activo; consultas a otros projectPath pueden carecer de watcher. Usar `status` y `sync` dirigidos cuando exista deriva, especialmente despues de pull, cambio de rama o generacion masiva. No suponer un indice siempre fresco.
Un subdirectorio sin indice puede resolverse contra un ancestro indexado: comprobar la raiz realmente resuelta y no tratar una subcarpeta como una aplicacion aislada por pasar projectPath. Mantener las aplicaciones en sus repos propios e inicializar el indice de cada una antes de consultar; no interpretar un resultado vacio como prueba de que su codigo no existe.
Ausencia de relaciones o tests en el grafo no prueba su inexistencia. En la prueba inicial del workspace el grafo no encontro algunos enlaces a tests aunque el suite Python ejecutaba 43 pruebas; imports dinamicos y otras construcciones requieren inspeccion dirigida. Rutas Spring, inyeccion de dependencias, metaprogramacion Django y enlaces frontend/backend pueden quedar parciales. Verificar contratos y comportamiento con pruebas reales.
La navegacion consulta codigo; no autoriza cambios ni ejecucion, y no sustituye SDD/OpenSpec, revision o aceptacion. El servidor puede escribir su indice local y metadatos aunque sus herramientas expuestas sean de lectura del codigo.

## Disponibilidad real

Hay tres estados distintos: dependencia instalada, MCP configurado en esa maquina y herramienta cargada en la sesion. Comprobar cada uno; un archivo de configuracion no prueba los tres. En la configuracion comun exponer solo `codegraph_explore`, mantener telemetria desactivada y usar rutas resueltas por la instalacion local.
Para nuevos proyectos, importar las instrucciones de AI-Workspace desde AGENTS.md del producto con una ruta accesible y commit consumido. No copiar wrappers aislados que dependan de enlaces relativos al repo original. La configuracion global de Codex hace el MCP disponible en ese equipo; no indexa cada proyecto ni instala otros skills o perfiles. Los subagentes deben tener acceso real a la herramienta o recibir contexto del padre; no asumir que una instruccion les concede herramientas.

## Instalacion y continuidad

Seguir [guia](../../docs/codegraph.md). Versionar dependencia, lockfile, scripts, skill y reglas. Excluir `.codegraph/`, `.codegraph-*/`, node_modules y bases generadas de Git. Al cambiar de equipo: pull, npm ci, registrar MCP local, abrir una sesion que lo cargue y construir indice del proyecto. No sincronizar SQLite ni rutas absolutas de otra maquina.
El launcher `scripts/codegraph.mjs` resuelve el paquete desde AI-Workspace y conserva el directorio del llamador; pasar aun asi el proyecto explicitamente. Evitar indexar home, unidades completas, datos comerciales generados o carpetas de terceros. Respetar exclusiones del repositorio y confirmar que el indice no se agregue a Git.

Fuentes consultadas el 2026-10-19: [CodeGraph](https://github.com/colbymchenry/codegraph), [instalacion](https://github.com/colbymchenry/codegraph/blob/main/site/src/content/docs/getting-started/installation.md), [variante utilizada por Gentle-AI](https://github.com/Gentleman-Programming/gentle-ai/blob/main/internal/components/communitytool/tool.go). Comandos y esquema MCP comprobados contra el paquete instalado 1.6.2; no garantizar equivalencia con versiones futuras.
