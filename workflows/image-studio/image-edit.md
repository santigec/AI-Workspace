# Edición de imagen

## Activación y entrada

Editar una imagen existente con cambios concretos y elementos que deben conservarse. Requiere original accesible y solicitud; para impresión añade la ficha confirmada.

## Etapas

1. image-analysis: identificar contenido y cambios.
2. preserve-original-art: determinar si se requiere fidelidad exacta. Si una herramienta generativa no puede garantizarla, elegir una operación determinista o bloquear esa transformación.
3. image-editing: producir un derivado y comparar con el original.
4. resize-to-print: solo cuando se soliciten dimensiones físicas de impresión.
5. print-ready-qa: solo para entrega de impresión; usar el archivo final y ficha completa.

## Salida

Archivo editado, comparación, cambios y limitaciones.
Una edición digital puede terminar tras la comparación. No exigir especificaciones de impresión a una imagen destinada solo a pantalla.
Si falla una restricción crítica, devolver FAIL y conservar el original.
