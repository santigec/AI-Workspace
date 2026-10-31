# Catálogo de productos

Medidas propuestas: taza 205 × 95 mm; tomatodos de 500, 600 y 750 ml con 232 × 125, 232 × 142 y 232 × 182 mm. No son dimensiones universales ni especificaciones aprobadas.
Todos los registros empiezan unverified. Camisetas, stickers y agendas tienen registros pendientes, sin medidas inventadas. Los .yaml usan JSON compatible con YAML 1.2.
El 2026-10-15 el usuario confirmó el lienzo de diseño para su tomatodo de 500 ml: **232 × 125 mm**, plano y continuo. El registro conserva unverified porque aún faltan modelo/proveedor y otros parámetros de producción; esto no impide generar un borrador con el tamaño indicado.
También confirmó el lienzo de **600 ml: 232 × 142 mm**, plano y continuo. Ambas confirmaciones corresponden al tamaño de su flujo de diseño; el registro de producción conserva unverified por los parámetros aún pendientes.
Para **750 ml confirmó 232 × 182 mm**, también plano y continuo. La misma distinción entre lienzo definido y ficha de producción completa aplica a las tres capacidades.

El 2026-10-19 el usuario definió para su tarrito cuadrado de 45 × 45 × 80 mm un adhesivo plano continuo de **180 × 80 mm**, organizado en cuatro paneles de 45 × 80 mm. El registro permanece `unverified` porque faltan proveedor, plantilla, sangrado, solape, tolerancias y parámetros de impresión.

El 2026-10-31 el usuario definió para una mochila de cordón un lienzo **A3 vertical de 297 × 420 mm**. El 25% superior, **y = 0–105 mm**, debe pintarse pero no contener información crítica porque se corruga con el cordón. La banda inferior propuesta **y = 350–420 mm** recibe logotipos o texto proporcionado. El producto permanece `unverified` hasta confirmar plantilla, costuras, sangrado, margen y espejo.

Para verificar un modelo completa supplier, model, verification.source, verified_by, verified_at, dimensiones y todos los campos production. Solo entonces cambia status a verified. La aprobación corresponde a un modelo y proveedor concretos.
print_area describe el rectángulo disponible dentro del lienzo; excluded_zones enumera restricciones. El ejecutor debe comprobar geometría y zonas excluidas; el validador no inspecciona imágenes.

Consulta [registro](../../../registry/products.yaml), [schema](../../schemas/product-catalog.schema.json) y [ficha](../../templates/product-spec.md).
