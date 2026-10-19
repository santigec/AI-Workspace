---
name: angular-development
description: Construye y revisa funcionalidades Angular con contratos HTTP, estados de interfaz y compatibilidad del proyecto.
---

# Desarrollo Angular

## Alcance y entradas

Aplicar a funcionalidades, correcciones y revisiones del frontend Angular.
Recibir escenario, criterios de aceptación, diseño disponible y contrato API del backend Spring.
Leer el [proceso](../../standards/institutional-process.md), el
[estándar Angular](../../standards/angular.md) y la [política de evidencia](../../standards/evidence-policy.md).

## Acciones

1. Identificar Angular, CLI, Node, TypeScript, RxJS, gestor y lockfile desde el repositorio y CI.
   Contrastar su matriz compatible antes de usar APIs; ejecutar herramientas locales del proyecto.
   No actualizar dependencias, convertir arquitectura ni instalar CLI global como efecto lateral.
2. Implementar un caso de uso vertical con componentes, servicios y rutas de la funcionalidad.
   Conservar standalone o NgModules y patrones de estado/formularios existentes; justificar cambios.
3. Acordar DTO de entrada/salida, nulabilidad, fechas, paginación, errores y permisos con el contrato
   Spring. Encapsular HTTP en servicios tipados; el genérico de HttpClient no valida JSON en runtime.
4. Revisar ciclo de suscripciones, cancelación y peticiones duplicadas; usar mecanismos disponibles
   en la versión del proyecto. Evitar retries que repitan mutaciones sin una garantía de idempotencia.
5. Implementar carga, vacío, éxito, validación y error con recuperación observable. Diferenciar
   401 de 403 según el contrato; evitar bucles de autenticación y envíos duplicados de formularios.
6. Mantener controles semánticos, etiquetas, foco, navegación por teclado y mensajes comprensibles.
   Revisar el flujo con teclado; registrar el alcance comprobado sin declarar certificación accesible.
7. Usar bindings y sanitización de Angular; no aplicar bypassSecurityTrust para ocultar errores.
   No incluir secretos de servidor en bundles; guards y botones ocultos no sustituyen autorización API.
8. Ejecutar build y pruebas pertinentes con scripts locales y lockfile existente. Cargar angular-testing
   para pruebas específicas; verificar integración real cuando el alcance incluya el recorrido completo.

## Evidencia de salida

- Caso de uso, contrato y versiones detectadas; cambios de UI/servicios y decisiones relevantes.
- Build, pruebas y revisión de estados/teclado ejecutados con resultados y limitaciones.
- Para integración, identificar builds/revisiones frontend y backend; diferenciar backend real de mock.

## Límites

No suponer compatibilidad de ejemplos actuales con la versión instalada.
No introducir biblioteca de estado, diseño o validación sin necesidad y compatibilidad demostradas.
La compilación TypeScript no demuestra comportamiento de navegador ni cumplimiento del contrato real.

## Referencias

[Fuentes y procedencia](../../knowledge/engineering-sources.md).
- [Compatibilidad Angular](https://angular.dev/reference/versions).
- [HttpClient y límites del tipado](https://angular.dev/guide/http/making-requests).
- [Seguridad Angular](https://angular.dev/best-practices/security).
- [Accesibilidad Angular](https://angular.dev/best-practices/a11y).
