# Evaluación

## Qué verificamos

La validación estructural comprueba registro, rutas, dependencias y referencias de casos. La evaluación de comportamiento comprueba decisiones y artefactos producidos por un modelo o persona usando el skill.

Ejecuta desde la raíz:
```console
python scripts/validate_workspace.py
python -m unittest discover -s tests
```

El validador usa solo la biblioteca estándar de Python 3. El registro es JSON, una sintaxis válida de YAML 1.2, para evitar una dependencia de parsing.

## Ejecutar un caso

1. Lee case-00N.md y reúne las entradas indicadas. Si requieren archivo real y no está disponible, registra NOT_RUN.
2. Ejecuta la solicitud con el skill o workflow indicado y registra herramientas, modelo o ejecutor, fecha, commit y rutas o hashes de entradas.
3. Conserva salida y artefactos derivados. Revisa cada criterio de expected-results.md con evidencia.
4. Completa [la plantilla de resultado](../evals/result-template.md). No confundas el FAIL esperado del skill con el FAIL de una evaluación.
5. Una evaluación pasa cuando se cumplen los criterios, incluido bloquear correctamente una solicitud incompleta.

Los casos iniciales son escenarios de prueba derivados de necesidades del dominio, no ejecuciones reales. No representan productos aprobados ni resultados obtenidos.

## Promoción

Alpha: instrucciones revisadas y controles estructurales.
Beta: casos normales y negativos ejecutados, con evidencia revisable y fallos corregidos.
Stable: casos representativos reales documentados y repetibles, incluidos límites críticos del dominio, revisados por el responsable. Define cobertura según el riesgo; no uses una cantidad arbitraria de pruebas para inferir calidad.

## Ramas

develop integra esta base. main contiene la última versión publicada, que puede incluir skills alpha explícitamente identificados. Promover a main requiere revisar cambios y resultados; no modifica por sí solo el estado de los skills.
