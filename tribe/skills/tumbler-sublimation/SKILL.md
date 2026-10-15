---
name: tumbler-sublimation
description: Genera o adapta arte plano y continuo para tomatodos de 500 o 600 ml, resolviendo dimensiones por capacidad desde pedidos e imágenes del chat.
---

# tumbler-sublimation

## Entrada y producto

Recibe capacidad, temática, nombre/texto exacto si se solicita, fondo y referencias opcionales.
Para tomatodo de **500 ml**, usa product.id tumbler_500ml y lienzo de **232 mm de ancho × 125 mm de alto**, confirmado por el usuario el 2026-10-15.
Para **600 ml**, usa tumbler_600ml y **232 × 142 mm**, confirmado en la misma fecha. La entrada especializada es [tumbler-600ml-sublimation](../tumbler-600ml-sublimation/SKILL.md).
Esta confirmación define el tamaño del diseño para su flujo; no verifica por sí sola proveedor, modelo, márgenes, espejo ni parámetros térmicos.
Si el pedido dice solo tomatodo y la capacidad no está en el contexto, pregunta la variante. No intercambies las alturas de 500 y 600 ml ni confirmes por extrapolación una variante de 750 ml.
Lee [workflow](../../../workflows/tribe/tumbler-sublimation.md), [catálogo](../../knowledge/product-catalog/tumblers.yaml), [principios](../../standards/design-principles.md) y [resiliencia](../../policies/non-blocking-generation.md).

## Composición especializada

Produce una imagen **plana, continua y horizontal**, destinada a impresión y posterior sublimación. Un mockup de botella no sustituye el arte.
La proporción del lienzo 500 ml es 232:125 (1.856:1). Es más alto proporcionalmente que el formato de taza 205 × 95 mm: recompón para este espacio, no estires un diseño de taza ni cambies solo sus metadatos.
Para 600 ml la proporción es 232:142 (aproximadamente 1.634:1): utiliza la altura adicional redistribuyendo la composición, sin escalar verticalmente todo el arte.
Aprovecha ancho y altura con personajes, tipografía y entorno equilibrados. Si la referencia es vertical y se permite adaptación, redistribuye elementos conservando proporciones; evita un póster estrecho flotando entre grandes vacíos laterales.
Mantén texto, rostros y elementos esenciales dentro del área útil. Reserva las zonas de unión según la plantilla; no inventes una medida universal de solape o margen.
Extiende el fondo de forma coherente a lo largo del ancho. Cuando se pida continuidad de la unión lateral, armoniza los extremos sin duplicar ni cortar contenido esencial.
Si el producto exige compensación cónica o plantilla curva, usa su plantilla verificada; no deformes el rectángulo de la variante por suposición.

## Referencias y fondo

Imágenes opcionales para arte nuevo; original accesible necesario si hay que editar o preservar un diseño.
Clasifica cada referencia como contenido, estilo o fondo. Elimina UI, precio y ficha de capturas comerciales salvo petición explícita.
Respeta identidad, textos y detalles requeridos. No añadas nombres de trabajos anteriores.
Fondo: transparent, solid o themed. PNG puede tener fondo opaco.
Para themed requiere background_description; crea entorno acorde a temática, sin tapar los sujetos o texto.
Superficie blanca significa lienzo blanco opaco si se pide para el arte; no equivale a un mockup ni obliga a vacíos laterales. Si se habla de sustrato blanco y se pide PNG transparente, conserva la transparencia del archivo.
Mantén el lienzo de la variante al cambiar fondo: 232 × 125 mm para 500 ml o 232 × 142 mm para 600 ml.

## Ejecución y salida

Modela la orden con el [schema](../../schemas/order-schema.yaml), workflow tumbler-sublimation y requested_dimensions de la variante: 232 × 125 para 500 ml o 232 × 142 para 600 ml.
Consulta product-specs; usa image-generation para arte nuevo o image-analysis e image-editing para edición. Para fidelidad exacta, prefiere operaciones deterministas disponibles o informa los límites de una adaptación generativa.
Si el usuario pide diseño, genera y muestra la imagen; una orden o un brief no completa ese pedido.
Comprueba texto, composición horizontal, proporción, continuidad, dimensiones reales del archivo y fondo.
Si se exigen 300 ppp, el objetivo redondeado es **2740 × 1476 px** para 500 ml o **2740 × 1677 px** para 600 ml. No asumas 300 ppp cuando no esté especificado ni presentes interpolación como detalle real.
Si la herramienta no entrega las dimensiones objetivo, informa píxeles y resolución efectiva. Para tamaño físico exacto coloca el arte proporcionalmente en un documento de las dimensiones de la variante, indicando márgenes o recorte; no recortes elementos críticos.
Con ficha confirmada, aplica sublimation-layout, resize-to-print y print-ready-qa. No apliques espejo automáticamente: confirma quién lo realiza.
Entrega imagen visible y archivo descargable, tamaño, fondo, cambios y pendientes. Un borrador puede avanzar con requisitos de producción pendientes; PRINT_READY exige archivo final y QA real completo.
