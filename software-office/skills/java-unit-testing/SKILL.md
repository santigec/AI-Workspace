---
name: java-unit-testing
description: Diseña y ejecuta pruebas unitarias Java con JUnit y evidencia de runner; distingue aislamiento de integración real.
---

# java-unit-testing

Verificar reglas de negocio y comportamiento de unidades Java mediante oráculos explícitos.
Aplicar a código aislable; derivar casos del plan y de defectos reproducibles.
Las versiones de Java/JUnit/plugins deben corresponder al proyecto existente.

## Procedimiento

1. Leer requisitos y contratos de la unidad; identificar dependencias y fronteras de aislamiento.
2. Cubrir caminos relevantes, valores límite, errores y efectos observables según riesgo.
3. Usar dobles sólo para colaboradores apropiados; no probar únicamente que el mock devuelve su configuración.
4. Preferir aserciones de comportamiento; verificar interacciones cuando sean parte del contrato.
5. Relacionar cada caso con requisitos o defectos, manteniendo ID del runner.
6. Ejecutar el comando acordado del proyecto y capturar exit code, versiones, selección y reportes originales.
7. En Maven exigir failIfNoTests=true para la suite obligatoria y revisar filtros/skips efectivos.
8. Retener fallos y reruns; un éxito posterior no elimina un intento fallido.

## Artefactos obligatorios

- Casos implementados y trazados, con oráculos y límites de aislamiento.
- Comando exacto, commit, ambiente, tiempos, exit code, log y XML real del runner con hashes.
- Selección prevista/descubierta/ejecutada y skipped/aborted/not_run explícitos.
- Defectos reproducibles y cobertura JaCoCo si se pidió o ayuda a identificar huecos.

## Límites

Cobertura mide código ejecutado: no demuestra corrección ni requisitos satisfechos.
No usar cobertura como sustituto de aserciones ni fijar porcentajes universales.
Mocks de repositorios o H2 no acreditan integración con la DB productiva.
Pruebas deshabilitadas, excluidas o no descubiertas nunca son PASS.
JUnit informa resultados técnicos; no concede UAT ni aceptación formal.
Evidencia importada puede ser consistente y conservar procedencia no verificada.

## Fuentes primarias

- [JUnit reporting](https://docs.junit.org/6.1.3/advanced-topics/junit-platform-reporting.html).
- [JUnit disabled tests](https://docs.junit.org/6.1.3/writing-tests/disabling-tests.html).
- [Surefire: selección, failIfNoTests y skips](https://maven.apache.org/surefire/maven-surefire-plugin/test-mojo.html).
- [JaCoCo: contadores y límites](https://www.jacoco.org/jacoco/trunk/doc/counters.html).

## Referencias de trabajo

Leer [testing](../../standards/testing.md) para gates y clasificación.
Aplicar [evidence-policy](../../standards/evidence-policy.md) a reportes y conclusiones.
Consultar [institutional-process](../../standards/institutional-process.md) para formularios y responsables.
Usar [engineering-sources](../../knowledge/engineering-sources.md) para fuentes y vigencia.
