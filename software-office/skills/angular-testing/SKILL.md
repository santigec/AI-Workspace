---
name: angular-testing
description: Diseña y ejecuta pruebas Angular de componentes, servicios HTTP y recorridos de navegador diferenciando mocks de integración real.
---

# Pruebas Angular

## Alcance y entradas

Recibir requisitos, riesgos, casos esperados, frontend y backend objetivo con sus builds/revisiones.
Aplicar el [proceso](../../standards/institutional-process.md), el [estándar de pruebas](../../standards/testing.md),
la [política de evidencia](../../standards/evidence-policy.md) y el [estándar Angular](../../standards/angular.md).
Identificar runner y versiones Angular/CLI/Node/TypeScript/RxJS desde config, lockfile y CI.
La documentación actual usa Vitest para proyectos nuevos; Karma sigue soportado. No migrar el runner
ni instalar herramientas globales para ejecutar una prueba existente.

## Acciones

1. Elegir nivel según riesgo: lógica aislada, componente con TestBed, servicio con backend HTTP
   simulado o navegador con servidores reales. Vincular casos a requisitos y oráculos observables.
2. En componentes, comprobar interacción y DOM: validación, carga, vacío, error, recuperación,
   401/403 y teclado/foco cuando aplique. Evitar pruebas que solo repitan detalles privados del código.
3. En servicios HTTP usar HttpTestingController o API compatible con la versión instalada:
   verificar método, URL/parámetros, cuerpo y headers pertinentes; simular respuesta y errores,
   comprobar ausencia de peticiones pendientes. No presentar estas pruebas como llamadas al backend.
4. Cuando se configuren providers funcionales, respetar el orden requerido por la versión:
   configuración de HttpClient antes del backend de prueba. Comprobar interceptores usados realmente.
5. Para E2E Playwright, definir datos aislados, identidad, URLs, limpieza y servicios requeridos.
   Registrar qué API/identidad/DB son reales y qué se intercepta; un E2E con mocks tiene alcance parcial.
6. Usar locators por rol/nombre accesible o test IDs acordados y assertions que reintentan.
   Esperar estado observable; no usar sleep fijo para sincronizar. Comprobar consecuencia de acciones,
   no solo que el click se completó o apareció una pantalla.
7. Ejecutar la selección prevista y comparar descubiertos/ejecutados/excluidos; preservar fallos,
   skipped e intentos de retry. Un rerun exitoso no borra evidencia del fallo previo.
8. Registrar comando, exit code, versiones, navegador, frontend build/SHA y backend build/SHA
   o identificador verificable equivalente. Si hay cambios sin commit, conservar su identidad de build.
   Guardar reportes y trazas relevantes cuando se generen; no inventar evidencia ni commitear binarios.

## Evidencia de salida

- Mapa requisito → caso → resultado, alcance real y dobles usados.
- Reportes originales, logs, contexto del entorno e identificadores de ambos productos probados.
- Fallos y límites; si falta navegador/backend/DB, registrar NOT_RUN o error según política.

## Límites

No atribuir a una prueba HTTP simulada compatibilidad con Spring desplegado.
No equiparar revisión automática de accesibilidad con evaluación completa o certificación.
No declarar gate PASS con cero casos relevantes ejecutados o por existencia de archivos de test.

## Referencias

[Fuentes y procedencia](../../knowledge/engineering-sources.md).
- [Testing Angular y runners](https://angular.dev/guide/testing).
- [Pruebas HTTP Angular](https://angular.dev/guide/http/testing).
- [Locators Playwright](https://playwright.dev/docs/locators).
- [Assertions Playwright](https://playwright.dev/docs/test-assertions).
- [Trace Viewer](https://playwright.dev/docs/trace-viewer).
