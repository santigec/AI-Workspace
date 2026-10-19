---
name: spring-data-jpa
description: Implementa y revisa persistencia Spring Data JPA con transacciones, consultas, migraciones y pruebas de base de datos.
---

# Persistencia Spring Data JPA

## Alcance y entradas

Aplicar a entidades, repositorios, consultas y operaciones de negocio persistentes.
Recibir reglas, esquema, consultas afectadas y motor de base de datos; comprobar versiones reales
de Boot, Hibernate, driver y herramienta de migración antes de elegir APIs o sintaxis.
Seguir el [proceso](../../standards/institutional-process.md) y el
[estándar Java/Spring](../../standards/java-spring-boot.md).

## Acciones

1. Explicar invariantes, cardinalidades, nulabilidad y claves; respaldar reglas críticas con
   restricciones de base de datos además de validación de aplicación.
2. Definir la unidad transaccional del caso de uso en el servicio correspondiente. Revisar
   propagación, rollback, llamadas internas sin proxy y alcance real de readOnly.
   Evitar mantener transacciones abiertas durante llamadas remotas lentas sin justificación.
3. Elegir consultas y proyecciones según los datos requeridos. Revisar SQL y cantidad de consultas
   al recorrer relaciones; resolver N+1 con un plan de carga explícito por consulta cuando proceda.
4. Verificar paginación y orden estable; no combinar fetch de colecciones con paginación
   sin comprobar el SQL, memoria y resultado. Diseñar índices a partir de filtros, joins y orden.
5. Tratar actualizaciones concurrentes: comprobar si hacen falta versionado optimista, locks o
   restricciones únicas; definir cómo se comunica y recupera un conflicto.
6. Usar el mecanismo de migraciones existente. Crear cambios incrementales; considerar datos
   previos, compatibilidad durante despliegue y recuperación. No editar migraciones aplicadas.
7. Comprobar repositorios, restricciones, concurrencia y migraciones con el motor real o
   Testcontainers cuando el comportamiento dependa del motor; H2 no demuestra equivalencia SQL.
8. Ejecutar la prueba apropiada y revisar sus límites: un test con rollback automático puede
   ocultar errores que aparecen al hacer commit; forzar flush/commit cuando el riesgo lo requiera.

## Evidencia de salida

- Invariantes y frontera transaccional; consultas y plan de carga relevantes.
- Migraciones y estrategia de compatibilidad; pruebas ejecutadas con motor y resultados.
- Para rendimiento, consulta o medición reproducible antes/después; no prometer mejoras sin medir.

## Límites

No usar ddl-auto=update como estrategia de migración de producción.
No resolver N+1 convirtiendo todas las relaciones en EAGER ni exponer entidades como contrato HTTP.
No ejecutar cambios destructivos contra datos reales como parte de una prueba local.

## Referencias

[Procedencia de fuentes](../../knowledge/engineering-sources.md).
- [Transacciones Spring Data JPA](https://docs.spring.io/spring-data/jpa/reference/jpa/transactions.html).
- [Semántica de Transactional](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html).
- [Hibernate ORM: fetching y consultas](https://docs.hibernate.org/orm/current/userguide/html_single/).
- [Migraciones e inicialización Boot](https://docs.spring.io/spring-boot/how-to/data-initialization.html).
- [Testcontainers en Boot](https://docs.spring.io/spring-boot/reference/testing/testcontainers.html).
