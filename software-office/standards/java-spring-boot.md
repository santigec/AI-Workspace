# Estándar Java y Spring Boot

Estado inicial: alpha 0.1.0. Aplicar proporcionalmente al cambio y a las convenciones del proyecto.

## Compatibilidad antes de implementación

Registrar versiones detectadas y origen: build/BOM, wrapper, toolchain, CI y runtime de destino.
Distinguir JDK que ejecuta el build del JDK de compilación y ejecución del producto.
Consultar documentación de la versión efectiva; current/latest son entradas de navegación, no pins.
No incorporar APIs o actualizar dependencias sin comprobar su compatibilidad conjunta.
Preferir la gestión de dependencias existente y documentar overrides cuando sean necesarios.

## Arquitectura e interfaces

Resolver casos de uso con módulos normales por capacidad de negocio y dependencias explícitas.
Distribuir servicios requiere una razón operativa o de dominio y costos de consistencia explicados.
Usar inyección por constructor y contratos de entrada/salida que no expongan entidades JPA.
Validar entradas, mantener errores estables y autorización sobre operación y recurso concreto.
La documentación API debe corresponder al contrato ejecutado; escoger OpenAPI/REST Docs según el proyecto.

## Datos y seguridad

Situar transacciones alrededor de invariantes del caso de uso y comprobar semántica de proxy/rollback.
Diseñar restricciones, índices y concurrencia; verificar carga de relaciones y consultas N+1.
Usar migraciones incrementales con el mecanismo existente y probarlas con un motor representativo.
No tratar ddl-auto=update como control de evolución del esquema productivo.
Elegir sesión u OAuth2 según clientes y proveedor existentes; no inventar configuración JWT.
Evaluar CSRF y CORS desde el flujo real. Mantener secretos y tokens fuera del código y logs.

## Verificación y operación

Seleccionar pruebas por riesgo: lógica sin contexto, slice para integración acotada y aplicación completa
cuando lo requiera el comportamiento. No imponer porcentajes de cobertura universales.
Usar wrapper y comandos de CI, registrar resultados y distinguir NOT_RUN de PASS.
Revisar empaquetado, configuración, salud y señales operativas relevantes cuando cambien.
Evitar cardinalidad sensible o ilimitada en métricas e instrumentación duplicada.
Para producción, explicar migraciones, compatibilidad durante despliegue y recuperación;
la preparación de estos artefactos no equivale a haber desplegado.

## Fuentes

- [Boot: requisitos](https://docs.spring.io/spring-boot/system-requirements.html).
- [JPA: transacciones](https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html).
- [Security: resource server JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html).
- [Boot: migraciones](https://docs.spring.io/spring-boot/how-to/data-initialization.html).
- [Boot: observabilidad](https://docs.spring.io/spring-boot/reference/actuator/observability.html).
