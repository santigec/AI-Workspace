---
name: mug-sublimation
description: Genera o adapta arte plano para una taza desde un pedido de chat, con referencias opcionales y fondo transparente, sólido o temático.
---

# mug-sublimation

## Entrada desde chat

Recibe nombre/texto exacto, temática, estilo, ancho y alto en mm, tipo de fondo y referencias adjuntas si existen.
Usa [el workflow](../../../workflows/tribe/mug-sublimation.md), [catálogo](../../knowledge/product-catalog/README.md), [principios](../../standards/design-principles.md) y [resiliencia](../../policies/non-blocking-generation.md).
Las medidas explícitas del pedido definen el lienzo de diseño. Para este producto el catálogo propone 205 × 95 mm; esa medida no verifica otros parámetros de impresión.
Una imagen no es obligatoria para arte nuevo. Para editar o preservar un dibujo específico, exige el original accesible.
Clasifica cada imagen como original a editar, referencia de contenido, estilo o fondo. Una captura de ejemplo no exige copiar su UI ni reconstruir exactamente sus personajes.

## Fondo

output.background puede ser transparent, solid o themed. PNG es un formato: puede tener transparencia o fondo opaco.
Para themed exige background_description y usa las referencias de fondo si se adjuntan. Crea paisaje acorde a la temática, continuo y legible, sin tapar nombre ni sujetos.
Si se solicita añadir fondo a una versión existente, edita esa imagen preservando los elementos principales. Mantén las dimensiones y evita deformación.
No elimines el fondo por defecto. No cambies transparent a themed ni viceversa sin que lo indique el pedido.

## Superficie blanca

Cuando el pedido diga superficie blanca para el arte plano, usa output.background solid y background_description "Lienzo blanco opaco", manteniendo ancho y alto. No equivale a un mockup de taza.
Conserva fondos internos y colores que formen parte del diseño; añade blanco alrededor del arte, no sustituye automáticamente sus zonas negras o de color.
Si el usuario habla del material de la taza blanca y exige PNG transparente, distingue sustrato físico de fondo del archivo; conserva la transparencia solicitada.
Al usar una captura comercial como referencia, elimina precio, ficha, cursor y UI salvo que esos elementos formen parte del arte solicitado. No añadas nombres de pedidos anteriores a un nuevo diseño si no se solicitan.

## Ejecución y entrega

Para un diseño envolvente de taza, adapta la composición al ancho y alto solicitados; no basta colocar un póster vertical en el centro de un lienzo horizontal con grandes vacíos laterales.
Si la referencia es vertical y se permite adaptación, redistribuye texto e ilustración proporcionalmente y extiende elementos secundarios para aprovechar el ancho. Con superficie blanca conserva el blanco como base; no implica dejar los laterales vacíos.
Si se exige mantener exactamente la composición original, no la redistribuyas: explica el espacio lateral necesario y ofrece una alternativa. Nunca estires el original para llenar.
Revisa que el resultado se perciba como una banda horizontal para taza, además de verificar las dimensiones físicas del archivo de entrega.

Modela la orden conforme al [schema](../../schemas/order-schema.yaml). Guarda pedidos y archivos reales fuera de Git.
Consulta product-specs. Para arte nuevo usa image-generation; para edición image-analysis e image-editing. Inspecciona el resultado real y conserva el original.
Genera y muestra la imagen cuando se solicite diseño; devolver solo una orden no completa esa solicitud. Si la herramienta no está disponible, explica el bloqueo.
Verifica nombre, proporción, dimensiones en píxeles y fondo real. Si la herramienta no entrega los píxeles solicitados, informa la resolución efectiva; no anuncies 300 ppp ficticios.
Cuando necesites un lienzo físico exacto, coloca el PNG sin deformación en un documento de ancho/alto mm y explica cualquier margen o recorte de fondo. No recortes contenido crítico.
Para impresión usa sublimation-layout, resize-to-print y print-ready-qa con requisitos confirmados. Puedes entregar borrador visual aunque queden datos de producción pendientes.
Entrega imagen visible, archivo descargable, dimensiones, decisiones de fondo y limitaciones. PRINT_READY requiere QA completo; una imagen generada por sí sola no implica aprobación.
