# Pedidos y catálogo

order-schema.yaml es JSON Schema Draft 2020-12 en sintaxis JSON compatible con YAML. product-catalog.schema.json valida registros.
Los [ejemplos](../templates/orders/mug-draft.example.json) son sintéticos y para borrador. No contienen nombres reales ni imágenes de clientes.

Desde la raíz:
```console
python -m pip install -r requirements-dev.txt
python scripts/validate_order.py tribe/templates/orders/mug-draft.example.json
python -m unittest discover -s tests
```

workflow referencia un workflow del registro, no un skill. Las restricciones hard nunca se relajan por resiliencia.
output.background admite transparent, solid y themed; themed requiere background_description. artwork.reference_images es opcional y clasifica cada adjunto como content, style o background. No sustituye artwork.source cuando se edita un original.
workspace_ref debe ser un commit completo para producción; se compara con HEAD. En borradores puede ser null. El validador rechaza producción con cambios en archivos versionados.
La validación comprueba schema, catálogo, producto/workflow, dimensiones, salida y contradicciones reconocidas. Restricciones descriptivas requieren revisión del ejecutor.
La disponibilidad del original, fidelidad, transparencia, texto, zonas excluidas y QA se comprueban en ejecución.

Guarda pedidos reales, salidas y logs en un ejecutor separado. AI-Workspace versiona schemas, ejemplos y reglas.
Un futuro design-runner registra commit, entradas, herramientas, artefactos, adaptaciones y QA. Esta versión no crea ese ejecutor ni llama modelos.
