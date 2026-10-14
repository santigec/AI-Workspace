# mug-order-intake-001 — primer pedido real

## Alcance

Prueba lógica de entrada del workflow mug-sublimation y consulta de product-specs. No evalúa generación, layout ni QA visual.

## Solicitud

Taza estándar por sublimación, temática dinosaurios, nombre suministrado con tilde, estilo infantil, profesional y limpio. Arte plano y continuo en PNG transparente.
La orden operativa con el nombre se guarda fuera de este repositorio en el directorio local de ejecuciones. No se versionan pedidos de clientes.

## Resultado esperado

- Resolver mug-sublimation y product.id mug_standard.
- Conservar el nombre suministrado sin cambiar la tilde.
- Consultar el catálogo y distinguir 205 × 95 mm propuestos de medidas aprobadas.
- Generar una orden conforme al schema y una ficha con todos los campos y sus pendientes.
- DRAFT_ALLOWED para la entrada; production_ready false.
- Rechazar producción con resolución física ausente.
- No afirmar que se generó imagen ni que pasó QA.

## Resultado

[Informe ejecutado](result-001.md). PASS corresponde exclusivamente a esta prueba lógica; los casos visuales permanecen NOT_RUN.
