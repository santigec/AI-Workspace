# Ciclo de ingenieria — borrador experimental preservado

Estado: experimental, sin evaluacion integral. Conserva el conocimiento preparado para SITOP V2; no afirma que exista un equipo automatico ni una aplicacion validada. Aplicar primero [SDD/OpenSpec](sdd-openspec.md) y consultar [proceso institucional](../../software-office/standards/institutional-process.md).

1. `software-lifecycle` ubica estado y alcance; `requirements-engineering` relaciona solicitud F0 y RFS F1 con escenarios OpenSpec.
2. `software-estimation` prepara F2, supuestos y riesgos; `system-design` y `uml-modeling` documentan decisiones proporcionales.
3. `java-spring-boot`, `spring-data-jpa`, `spring-security` y `angular-development` se aplican segun codigo y stack reales, no todos por rutina.
4. `test-planning` prepara F3; `java-unit-testing`, `spring-integration-testing`, `angular-testing`, `api-contract-testing`, `security-testing` y `performance-testing` se eligen por riesgo y alcance autorizado.
5. `test-evidence` consolida evidencia real. Su validador/parser especializado sigue pendiente: ver [limites](../../software-office/standards/evidence-policy.md). `software-acceptance` prepara F4 para decision del requirente.
6. `production-release` prepara F5 y plan verificable de despliegue/rollback; no ejecutar produccion sin autorizacion concreta. Actualizar UML afectado, reportes, specs y memoria segun trabajo realizado.

Tribe Sport conserva SDD y trazabilidad, sin imponer F0-F5; este borrador institucional no reemplaza su futuro perfil Django/Railway. Roles especializados y prueba de flujo completo siguen pendientes.
