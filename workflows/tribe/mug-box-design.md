# Caja de taza temática

1. Ejecutar mug-box-design para recoger temática, textos solicitados y medidas de 150 × 200 mm. Registrar como propuesta cualquier extensión de reserva central que no esté confirmada por una plantilla.
2. Usar image-analysis si hay referencias: identificar paleta, lettering, emblemas y relación con la taza, excluyendo UI comercial.
3. Usar image-generation para arte nuevo o image-editing para modificar arte existente. Producir una sola composición plana vertical, fondo continuo, motivo central completo en y = 50–80 mm (máximo 30 mm), artes inferiores laterales y reservas centrales superior de 50 mm e inferior de 120 mm. Usar x = 45–105 mm como ancho central propuesto; solo fondo discreto en las reservas. La variante y = 40–80 mm requiere solicitud explícita.
4. Aplicar resize-to-print cuando sea necesario para maquetación física, conservando proporción, legibilidad y resolución efectiva; no convertir un reescalado en una afirmación de detalle nativo.
5. Revisar con print-ready-qa y el checklist tribe/templates/mug-box-qa.md. Mostrar imagen y archivo; indicar DRAFT si faltan parámetros de producción.

Invocación desde chat con el checkout accesible:

```text
$mug-box-design
Caja para taza de 150 × 200 mm.
Temática: [tema]. Usa la imagen adjunta como referencia.
Fondo y borde temáticos, colores vibrantes y tipografía del tema.
Artes abajo a izquierda y derecha; centro inferior libre.
Motivo central completo dentro de y = 50–80 mm desde arriba; altura máxima 30 mm.
Columna central propuesta x = 45–105 mm: 50 mm libres arriba y 120 mm libres abajo, solo fondo discreto.
Mantén los artes laterales fuera de esta columna y no desbordes con letras, cabello o humo protagonista.
Genera y muestra el arte plano y continuo.
```

No añade nombre por defecto. Si se solicita personalización, incorporar el texto exacto. La invocación depende de que el entorno tenga acceso a los archivos; el repositorio no instala automáticamente la skill en ChatGPT web.
