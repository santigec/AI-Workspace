---
name: performance-testing
description: Diseña y ejecuta pruebas de rendimiento con carga y criterios acordados, evidencia de k6 y límites autorizados.
---

# performance-testing

Evaluar requisitos de latencia, capacidad, errores y estabilidad en un contexto reproducible.
Relacionar métricas con operaciones de negocio y un modelo de carga sustentado.
No inventar objetivos, concurrencia o duración como criterios de aceptación.

## Procedimiento

1. Identificar requisitos/SLO, usuarios, operaciones, volumen de datos y patrón de tráfico.
2. Registrar objetivo y tipo de prueba: baseline, carga, estrés o duración, según alcance.
3. Confirmar entorno autorizado, recursos, dependencias, límites de carga y condiciones de parada.
4. Preparar datos, calentamiento y distribución de escenarios; justificar representatividad.
5. Definir thresholds desde requisitos acordados y checks funcionales de respuestas.
6. Ejecutar incrementalmente; comenzar con verificación no disruptiva y respetar límites.
7. Capturar métricas originales, configuración, carga alcanzada, duración, errores y saturación.
8. Analizar resultados contra criterios, diferencias del entorno y variación observada.

## Artefactos obligatorios

- Plan/modelo de carga con requisitos, thresholds, autorización y límites.
- Script y dataset identificados por hash; versiones de k6 y artefacto probado.
- Comando, tiempos, exit code, métricas/reportes originales y hashes.
- Comparación criterio/resultado, defectos, restricciones y escenarios no ejecutados.

## Límites

En k6 los checks solos no cambian exit status; usar thresholds para el gate acordado.
Exit 0 sin carga suficiente o sin métricas requeridas no demuestra cumplimiento.
Un umbral del ejemplo documental no es requisito del producto.
No extrapolar capacidad de producción desde ambientes no equivalentes sin análisis explícito.
Pruebas de estrés, resiliencia o producción necesitan límites y autorización concretos.
No generar tráfico externo ni costes fuera del alcance autorizado.
Datos insuficientes, interrupción o NOT_RUN permanecen inconclusos, nunca PASS.
El dueño del servicio acuerda SLO; operaciones valida capacidad/impacto y negocio acepta.

## Fuentes primarias

- [k6 thresholds, exit status y checks](https://grafana.com/docs/k6/latest/using-k6/thresholds/).
- [Spring Boot: servidor real para pruebas HTTP](https://docs.spring.io/spring-boot/reference/testing/spring-boot-applications.html).
- [ISO 29119: diseño y procesos de prueba](https://committee.iso.org/sites/jtc1sc7/home/projects/flagship-standards/isoiecieee-29119-series.html).

## Referencias de trabajo

Leer [testing](../../standards/testing.md) para gates y clasificación.
Aplicar [evidence-policy](../../standards/evidence-policy.md) a reportes y conclusiones.
Consultar [institutional-process](../../standards/institutional-process.md) para formularios y responsables.
Usar [engineering-sources](../../knowledge/engineering-sources.md) para fuentes y vigencia.

