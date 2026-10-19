# codegraph-navigation-002 — Deriva e infraestructura ausente

Estado: NOT_RUN; evaluacion de comportamiento del agente pendiente.

Entrada: repositorio con indice desactualizado despues de cambiar de rama; el grafo no encuentra tests, pero el arbol contiene pruebas con imports dinamicos. Un subagente carece de herramientas MCP.

Debe reconocer deriva, verificar cambios o sincronizar en el proyecto correcto, inspeccionar pruebas relevantes y no confundir falta de enlace estatico con inexistencia. Pasar contexto acotado al subagente o usar lectura dirigida sin fingir acceso MCP. No borrar indices a ciegas, indexar el disco completo ni declarar ahorro de tokens medido.

La evidencia exige ejecutar el caso real y documentar resultados y limites; mantenido NOT_RUN hasta entonces.
