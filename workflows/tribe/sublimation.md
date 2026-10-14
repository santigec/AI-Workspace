# Sublimación

## Activación

Preparar arte para sublimación de un producto identificado. "Una taza" sin modelo ni área imprimible inicia la recopilación de datos, no una salida de producción.

## Entrada

Imagen original accesible, intención de adaptación y ficha del producto con medidas, área imprimible, fondo, resolución, color y política de espejo confirmados.

## Etapas

1. image-analysis: describir arte y restricciones; detener si no puede inspeccionarse.
2. product-specs: completar la ficha con fuentes; detener ante requisitos críticos pendientes.
3. sublimation-layout: adaptar al área imprimible preservando contenido; si necesita reescalado, usar resize-to-print.
4. print-ready-qa: revisar el archivo final contra la ficha y el original.

## Salida

Archivo derivado, ficha usada, decisiones de ajuste, recorte y espejo, e informe QA.
PASS: todos los requisitos críticos cumplidos. PASS WITH WARNINGS: solo advertencias no críticas documentadas. FAIL: requisitos incumplidos o verificaciones críticas pendientes.
No aplicar parámetros térmicos como parte de este workflow.
