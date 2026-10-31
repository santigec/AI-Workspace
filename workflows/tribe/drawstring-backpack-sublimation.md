# Mochila de cordón A3

1. Ejecutar drawstring-backpack-sublimation con `product.id: drawstring_backpack_a3`, temática, referencias, textos y logotipos exactos solicitados.
2. Usar image-analysis cuando haya referencias para separar contenido, estilo y fondo, excluyendo marcos de captura y elementos comerciales ajenos.
3. Usar image-generation para arte nuevo o image-editing para preservar un original. Producir una sola composición plana A3 vertical de 297 × 420 mm.
4. Mantener y = 0–105 mm completamente pintado pero sin contenido crítico porque corresponde al 25% superior corrugable. Centrar el motivo principal debajo de esa franja. Reservar como propuesta y = 350–420 mm para logotipos o texto proporcionado; si no existen, conservar fondo temático discreto.
5. Aplicar resize-to-print solo para maquetación física, sin presentar el remuestreo como detalle nativo ni recortar elementos esenciales.
6. Revisar con print-ready-qa: orientación, dimensiones, franja corrugable, fondo completo, legibilidad, borde, banda inferior y archivo real. Entregar DRAFT mientras falten plantilla, sangrado, margen, costuras o espejo.

Invocación desde chat con el checkout accesible:

```text
$drawstring-backpack-sublimation
Mochila de cordón en A3 vertical, 297 × 420 mm.
Usa la imagen adjunta como referencia.
Pinta todo el lienzo; deja y = 0–105 mm solo con fondo o borde discreto.
Centra el motivo principal en la zona visible y reserva y = 350–420 mm para los logotipos entregados.
Genera y muestra el arte plano, sin mockup ni espejo.
```
