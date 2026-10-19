# Primer equipo operativo de Tribe

Tres roles, veintiún skills reutilizables. Los agentes ejecutan/coordinaran tareas; los skills contienen el conocimiento de dominio. Las herramientas de generación y revisión deben estar disponibles en la sesión. No hay empleados autónomos permanentes ni proceso de fondo.

| Rol | Entrada | Salida |
|---|---|---|
| coordinador | Pedido y memoria pertinente | Brief, criterios de aceptación, asignación y entrega consolidada |
| disenador | Brief + skill de producto | Arte/propuesta y evidencia de medidas/verificaciones |
| revisor | Brief + artefacto real | Hallazgos independientes, evidencia y correcciones |

Perfiles nativos de proyecto: `.codex/agents/*.toml`, sin imponer modelo ni razonamiento. Heredan ajustes y permisos de la sesión. Un rol de revisor sin edición es una instrucción de comportamiento, no un sandbox independiente.

## Recorrido

1. Coordinador: RECIBIDO, fija producto, tema, dimensiones, personalización y entregables, y distingue datos críticos pendientes de decisiones reversibles.
2. Diseñador: EN_DISENO, ejecuta con el skill de producto; entrega arte y verificaciones. En una prueba de lectura solo inspecciona, no genera arte nuevo.
3. Revisor: EN_REVISION, abre el resultado y comprueba lo pedido. No aprobar un archivo por el relato del diseñador.
4. Si hay fallos, REQUIERE_CAMBIOS con corrección acotada. Diseñador corrige y revisor vuelve a verificar; máximo dos rondas antes de reportar el requisito pendiente.
5. Coordinador: ENTREGADO con evidencia y limitaciones; esto no es sinónimo de PRINT_READY.
6. Hilo principal: guarda aprendizajes en Engram y publica solo conocimiento, no imágenes/PDF/ZIP.

Un mismo hilo principal puede actuar como coordinador usando su perfil y delegar a diseñador/revisor. Si el usuario quiere observar los tres, delegar también la preparación del brief a un subagente coordinador y mantener la orquestación desde el principal. No duplicar equipos anidados. Esperar la salida de una etapa antes de iniciar la siguiente; solo comprobaciones independientes se pueden paralelizar.

## Cómo activarlo

```text
Usa el equipo coordinador, disenador y revisor para este pedido.
Producto: [taza/tomatodo/agenda]. Tema y referencias: [adjuntas].
Personalización: [solo si se pide]. Entrega: [lo solicitado].
Muéstrame qué hace cada agente y el resultado de la revisión.
```

Para una prueba sin crear imágenes: «Usa los tres agentes para revisar un diseño existente, sin modificarlo». La aplicación puede mostrar los hilos de subagentes; en CLI usar /subagents. Si una sesión no descubrió los perfiles recién añadidos, abrir un chat nuevo dentro del proyecto o pasar las instrucciones del perfil a la delegación. No confundir esa carga manual con una prueba de descubrimiento nativo.

Estados visibles son reportes del coordinador y de los hilos, no un dashboard web implementado. No crear un tablero ficticio ni afirmar ejecución de agentes que no se delegaron realmente.

Fuente de formato de agentes: https://learn.chatgpt.com/docs/agent-configuration/subagents
