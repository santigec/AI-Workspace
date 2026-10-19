---
name: java-spring-boot
description: Construye y revisa aplicaciones Java con Spring Boot respetando la arquitectura, versiones y pruebas del proyecto.
---

# Java y Spring Boot

## Alcance y entradas

Aplicar a funcionalidades, correcciones y revisiones de aplicaciones Spring Boot.
Recibir el caso de uso, criterios de aceptación y repositorio; inferir convenciones desde código y CI.
Leer el [proceso institucional](../../standards/institutional-process.md) y el
[estándar Java/Spring](../../standards/java-spring-boot.md) según el alcance del cambio.

## Acciones

1. Identificar Java de compilación y ejecución, Boot/BOM, Framework, wrapper Maven/Gradle,
   dependencias relevantes y versiones de CI. Registrar incompatibilidades antes de elegir APIs.
2. Consultar documentación correspondiente a esa matriz. No actualizar versiones automáticamente
   ni asumir que ejemplos de Boot 4 funcionan en Boot 3.
3. Traducir el caso de uso a entrada, reglas, salida, errores y autorización comprobables.
   Implementar un recorrido vertical pequeño con pruebas de sus riesgos.
4. Mantener módulos por capacidad de negocio y dependencias explícitas. Usar inyección por
   constructor; evitar infraestructura distribuida sin una necesidad demostrada.
5. Separar DTO y entidades persistentes, validar entradas y conservar el contrato de errores.
   Usar configuración tipada cuando aporte validación y evitar secretos en código o logs.
6. Revisar límites de transacción, consultas, migraciones y autorización cuando el cambio los toque;
   cargar los skills spring-data-jpa o spring-security si se necesita su procedimiento especializado.
7. Mantener logs útiles sin datos sensibles y observabilidad proporcional: salud, métricas o trazas
   donde permitan detectar el fallo del caso de uso. Evitar instrumentación duplicada.
8. Ejecutar los comandos del wrapper y CI pertinentes desde la raíz correcta; comprobar pruebas,
   empaquetado y configuración afectada. Diferenciar fallo del producto de dependencia no disponible.

## Evidencia de salida

- Caso de uso y decisiones relevantes, archivos modificados y matriz detectada.
- Comandos ejecutados con resultado y comportamiento comprobado, incluidos errores relevantes.
- Riesgos pendientes, requisitos no verificables y pasos de operación si cambian.

## Límites

No declarar ejecución, integración o preparación para producción sin evidencia.
Respetar el build existente; no añadir Lombok, cache, bases adicionales o microservicios por plantilla.
Una revisión ordinaria no implica migración de stack ni despliegue.

## Referencias

Consultar el [catálogo de fuentes](../../knowledge/engineering-sources.md) para procedencia y criterios.
- [Requisitos de Spring Boot](https://docs.spring.io/spring-boot/system-requirements.html).
- [Spring Modulith: módulos lógicos](https://docs.spring.io/spring-modulith/reference/fundamentals.html).
- [Observabilidad de Boot](https://docs.spring.io/spring-boot/reference/actuator/observability.html).
- [Compatibilidad Gradle](https://docs.gradle.org/current/userguide/compatibility.html).
- [Maven Toolchains](https://maven.apache.org/guides/mini/guide-using-toolchains.html).
