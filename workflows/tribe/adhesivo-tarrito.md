# Adhesivo tematico para tarrito cuadrado

1. Ejecutar `adhesivo-tarrito` para recoger tematica, textos exactos, referencias y caracter visual solicitado.
2. Confirmar el lienzo de 180 x 80 mm y mapear P1-P4 como cuatro zonas contiguas de 45 x 80 mm. Mantener las uniones x = 45, 90 y 135 mm libres de contenido critico.
3. Usar image-analysis si hay referencias. Separar identidad visual valida de UI, precios u otros elementos comerciales.
4. Usar image-generation para arte nuevo o image-editing para adaptar un original. Generar una sola banda continua, con fondo coordinado y un foco centrado en cada panel.
5. Inspeccionar el arte completo y cada panel con `tribe/templates/adhesivo-tarrito-qa.md`. Mostrar la imagen y el archivo real.
6. Usar resize-to-print y print-ready-qa solo con requisitos confirmados. Declarar DRAFT mientras falten plantilla, sangrado, solape, tolerancias o parametros de impresion.

Invocacion orientativa:

```text
$adhesivo-tarrito
Tematica: [tema]. Caracter visual: [delicado/divertido/otro].
Genera y muestra un arte plano continuo de 180 x 80 mm, dividido conceptualmente en cuatro caras de 45 x 80 mm, cada una con su foco centrado.
```

No añade nombres ni frases por defecto. Los archivos reales de pedidos quedan fuera de Git.
