---
name: resize-to-print
description: Ajusta dimensiones de arte para impresión con tamaño físico y resolución confirmados.
---

# resize-to-print

Confirma ancho, alto, unidades, resolución requerida y política de ajuste: contener, recortar o ampliar lienzo.
Calcula píxeles = mm / 25.4 × ppp, redondeando al entero más cercano.
Preserva proporción salvo que se solicite deformación. No confundas cambiar metadatos con aumentar detalle.
Si el original queda corto de resolución, informa la resolución efectiva y cualquier interpolación.
Entrega el archivo derivado con dimensiones físicas, píxeles, resolución y política de ajuste usada.
