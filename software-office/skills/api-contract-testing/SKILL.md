---
name: api-contract-testing
description: Verifica contratos HTTP o mensajería entre consumidor y productor con versiones trazables; no sustituye integración desplegada.
---

# api-contract-testing

Comprobar compatibilidad de interacciones acordadas y sus resultados observables.
Aplicar a contratos ejecutables de consumidores/productores y cambios compatibles o incompatibles.
Un documento OpenAPI validado estructuralmente no demuestra cumplimiento del servicio.

## Procedimiento

1. Identificar propietario, consumidor, productor y versión exacta del contrato.
2. Fijar casos de solicitud/respuesta o mensaje, códigos, esquemas y semántica exigida.
3. Incluir casos negativos, campos opcionales, errores y compatibilidad según requisitos.
4. Verificar el productor contra el contrato mediante pruebas ejecutables y base de prueba inspeccionada.
5. Verificar consumidor contra stubs derivados del contrato exacto; registrar su origen y digest.
6. Si se requiere proveedor desplegado real, ejecutar integración separada contra ese objeto.
7. Capturar comandos, runner, selección, reportes, exit code e identidad de los artefactos.
8. Tratar cambios incompatibles como defecto/decisión explícita del dueño del contrato.

## Artefactos obligatorios

- Contrato versionado con digest, propietarios y requisitos vinculados.
- Matriz de versiones consumidor/productor/stub y casos REQ -> TEST -> RESULT.
- Reportes originales del productor y consumidor con hashes, logs y procedencia.
- Diferencias de compatibilidad, defectos y alcance real de cada verificación.

## Límites

Un stub simula al colaborador; no acredita que el proveedor desplegado responda igual.
No publicar stubs de implementación no verificada como evidencia de productor conforme.
No usar versiones dinámicas como '+' para identificar evidencia formal.
Generación de pruebas o stubs no implica que se ejecutaron.
Validación de esquema, contrato ejecutado e integración desplegada son afirmaciones distintas.
Skipped/not_run nunca son PASS; evidencia importada no autentica por sí misma la ejecución.
Los responsables de ambas interfaces acuerdan compatibilidad; la skill no aprueba cambios por ellos.

## Fuentes primarias

- [Spring Cloud Contract: productor y consumidor](https://docs.spring.io/spring-cloud-contract/reference/getting-started/three-second-tour.html).
- [Spring Boot testing: infraestructura mock y real](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html).
- [JUnit reporting](https://docs.junit.org/6.1.3/advanced-topics/junit-platform-reporting.html).

## Referencias de trabajo

Leer [testing](../../standards/testing.md) para gates y clasificación.
Aplicar [evidence-policy](../../standards/evidence-policy.md) a reportes y conclusiones.
Consultar [institutional-process](../../standards/institutional-process.md) para formularios y responsables.
Usar [engineering-sources](../../knowledge/engineering-sources.md) para fuentes y vigencia.

