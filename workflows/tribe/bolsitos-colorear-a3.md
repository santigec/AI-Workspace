# Bolsitos para colorear A3

1. Ejecutar `bolsitos-colorear-a3` con `product.id: drawstring_backpack_coloring_a3`, referencia, temática y textos exactos solicitados.
2. Usar `image-analysis` para identificar personajes, pose, vestuario, objetos, título y ornamentos; excluir UI y elementos comerciales ajenos.
3. Redibujar con `image-generation` o `image-editing` una sola composición plana A3 vertical de 297 × 420 mm como line art negro puro sobre fondo blanco, con contornos cerrados y espacios amplios para colorear.
4. Mantener y = 0–105 mm sin contenido crítico y solo con ornamentos delineados dispersos. Centrar el motivo debajo de esa franja y reservar y = 350–420 mm para lettering hueco o decoraciones simples.
5. Evitar color, grises, sombras, degradados, semitonos, tramados, texturas, grandes rellenos negros y microdetalle ruidoso.
6. Aplicar `resize-to-print` solo para maquetación física, sin presentar el resultado como detalle nativo ni recortar elementos esenciales.
7. Revisar con `print-ready-qa` orientación, dimensiones, franja corrugable, line art, contornos, legibilidad y archivo real. Entregar DRAFT mientras falten plantilla física, sangrado, margen, costuras, espejo o QA de impresión.

Invocación desde chat:

```text
$bolsitos-colorear-a3
Mochila de cordón para colorear en A3 vertical, 297 × 420 mm.
Usa la imagen adjunta como referencia y redibújala con líneas negras limpias sobre blanco.
Deja y = 0–105 mm sin contenido crítico, centra el motivo debajo y usa lettering hueco en la banda inferior.
Genera y muestra el arte plano, sin color, sombras, mockup ni espejo.
```
