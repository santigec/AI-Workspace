---
name: spring-integration-testing
description: Prueba integración Spring Boot con API y dependencias reales, incluidas bases de datos; exige evidencia del ambiente y runner.
---

# spring-integration-testing

Verificar conexiones entre aplicación, servidor HTTP, persistencia y servicios incluidos en alcance.
Distinguir slices, mock web, contratos con stubs e integración de servicios reales.
Usar la configuración compatible del proyecto; no actualizar dependencias como efecto lateral.

## Procedimiento

1. Identificar rutas de negocio, componentes reales, dobles y fallos que deben observarse.
2. Para API HTTP real, iniciar servidor con RANDOM_PORT/ambiente equivalente y cliente real.
3. Usar motor DB y versión acordados; Testcontainers puede proporcionar dependencias desechables.
4. Registrar digest de imagen, migraciones, dataset, configuración saneada y modo de conexión.
5. Probar persistencia observable, restricciones, transacciones y comportamiento ante fallos relevantes.
6. Aislar datos y definir limpieza explícita: el rollback del test no limpia transacciones del servidor HTTP.
7. En Maven configurar Failsafe integration-test + verify y ejecutar el lifecycle verify completo.
8. Exigir failIfNoTests=true para suites obligatorias; registrar flags, perfiles, filtros y skipped.

## Artefactos obligatorios

- Matriz REQ -> TEST -> RESULT y mapa de componentes reales frente a dobles.
- Identidad exacta de aplicación/classes probadas, ambiente, DB, migraciones y datos.
- Comando, inicio/fin, exit code, logs, XML de casos y resumen Failsafe originales con hashes.
- Defectos y diferencias conocidas frente a producción, incluidos límites de equivalencia.

## Límites

@SpringBootTest usa MOCK por defecto y no inicia servidor HTTP.
MockMvc/WebMvcTest no acreditan una llamada de red ni integración con DB real.
H2 no sustituye evidencia del motor requerido; un contenedor no reproduce toda producción.
Finalizar integration-test con exit 0 no demuestra aprobación: falta verify.
DB/servicio no disponible produce error o NOT_RUN, nunca sustitución silenciosa por mocks.
Conservar lifecycle de contenedores compatible con caché del ApplicationContext.
Integración exitosa no sustituye aceptación del negocio ni autorización de despliegue.

## Fuentes primarias

- [Spring Boot testing: entornos y transacciones](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html).
- [Spring Boot Testcontainers](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html).
- [Testcontainers Java](https://java.testcontainers.org/).
- [Failsafe lifecycle y reportes](https://maven.apache.org/surefire/maven-failsafe-plugin/).

## Referencias de trabajo

Leer [testing](../../standards/testing.md) para gates y clasificación.
Aplicar [evidence-policy](../../standards/evidence-policy.md) a reportes y conclusiones.
Consultar [institutional-process](../../standards/institutional-process.md) para formularios y responsables.
Usar [engineering-sources](../../knowledge/engineering-sources.md) para fuentes y vigencia.

