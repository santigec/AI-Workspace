# Estándar Angular

Estado inicial: alpha 0.1.0. Aplicar proporcionalmente al cambio y a las convenciones del proyecto.
Complementa [testing](testing.md), [evidence-policy](evidence-policy.md) y el
[proceso institucional](institutional-process.md); no concede conformidad ni aceptación humana.

## Compatibilidad y estructura

Detectar Angular, CLI, Node, TypeScript, RxJS, gestor, lockfile y configuraciones de CI/build.
Comprobar matriz de versiones antes de elegir APIs; usar CLI y scripts locales del proyecto.
No introducir upgrades, instalaciones globales ni conversión standalone/NgModules por defecto.
Organizar por funcionalidad con responsabilidades claras y conservar convenciones vigentes.

## Contratos y experiencia

Coordinar DTO, rutas, verbos, nulabilidad, fechas, paginación, validación y errores con Spring.
El tipado de HttpClient describe una expectativa, no valida el JSON recibido en runtime.
Determinar necesidad de validación runtime por contrato y riesgo de la frontera, sin imponer librerías.
Definir estados de carga, vacío, éxito y error; permitir recuperación sin repetir mutaciones inseguras.
Comprobar 401/403, sesión/token y autorización real en backend; guards solo controlan navegación local.
Los formularios deben comunicar errores, mantener foco útil y prevenir envíos duplicados.
Revisar semántica HTML, etiquetas, teclado y mensajes; declarar alcance de accesibilidad evaluado.

## Seguridad

Preferir bindings y sanitización del framework; revisar usos de DOM directo, innerHTML y URLs dinámicas.
No introducir bypassSecurityTrust como solución general ni secretos en código, configuración o bundles.
No decidir persistencia de tokens, cookies, CORS o CSRF sin revisar el flujo conjunto con el backend.
Las validaciones cliente mejoran experiencia; el servidor conserva controles de datos y autorización.

## Verificación y evidencia

Conservar el runner existente; la documentación actual usa Vitest en proyectos nuevos y mantiene Karma.
Pruebas de componente/servicio y HTTP simulado no demuestran integración con Spring desplegado.
E2E debe identificar frontend y backend reales, versiones/builds, dobles, datos, navegador y alcance.
En Playwright usar locators estables y assertions con reintento; esperar condiciones, no tiempos fijos.
Guardar comando, resultado, casos omitidos, intentos y reportes/trazas disponibles según la política.
Mantener artefactos pesados fuera de Git; un enlace o hash aislado no autentica ejecución.
Los checks automáticos de accesibilidad no sustituyen evaluación manual ni otorgan certificación.
Un build correcto prueba compilación/empaquetado; no equivale a E2E, UAT o preparación de release.

## Fuentes

- [Angular: matriz de compatibilidad](https://angular.dev/reference/versions).
- [Angular: HTTP](https://angular.dev/guide/http/making-requests).
- [Angular: seguridad](https://angular.dev/best-practices/security).
- [Angular: accesibilidad](https://angular.dev/best-practices/a11y).
- [Angular: testing](https://angular.dev/guide/testing).
- [Angular: HTTP testing](https://angular.dev/guide/http/testing).
- [Playwright: assertions](https://playwright.dev/docs/test-assertions).
