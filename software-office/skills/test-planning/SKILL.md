---
name: test-planning
description: Diseña planes y guiones de prueba trazables para software; no declara ejecución ni aceptación.
---

# test-planning

Definir alcance verificable a partir de requisitos versionados, riesgos y criterios de negocio.
Usar para preparar o revisar plan, guion, matriz de trazabilidad y criterios de entrada/salida.
No confundir plan aprobado, pruebas implementadas y pruebas efectivamente ejecutadas.

## Procedimiento

1. Identificar versión de requisitos, objeto a probar, ambientes, responsables y restricciones.
2. Registrar supuestos pendientes; no inventar requisitos ni resultados esperados para completar casillas.
3. Diseñar escenarios positivos, negativos, fronteras, permisos y fallos según riesgo.
4. Para cada caso, identificar requisito, precondiciones, datos, pasos/estímulo y resultado esperado observable.
5. Definir oráculo, prioridad, nivel/tipo, dependencias y criterios de entrada/salida medibles.
6. Mapear cada requisito dentro de alcance a casos; justificar exclusiones y requisitos sin prueba.
7. Acordar responsabilidades de revisión, ejecución, defectos, UAT y decisión de liberación.
8. Vincular el Formulario 3 sólo mediante el mapeo institucional vigente; leer su fuente antes de usar campos.

## Artefactos obligatorios

- Plan y guion versionados, con fuentes de requisitos y supuestos pendientes.
- Matriz REQ -> TEST; identificación de datos, ambientes, responsables y criterios acordados.
- Registro de revisión con referencia real; si no existe, indicar pendiente.
- Manifiesto de casos previstos para comparar después con descubrimiento y ejecución.

## Límites

Un caso escrito queda NOT_RUN hasta contar con ejecución corroborada.
No imponer cobertura universal ni umbrales no funcionales sin requisito/riesgo acordado.
No atribuir a los formularios campos que no se hayan inspeccionado.
El negocio valida necesidades y aceptación; QA revisa suficiencia del diseño y trazabilidad.

## Fuentes primarias

- [ISO 29119: procesos, documentación y técnicas](https://committee.iso.org/sites/jtc1sc7/home/projects/flagship-standards/isoiecieee-29119-series.html).
- [ISO/IEC/IEEE 29119-1:2022, conceptos gratuitos](https://www.iso.org/standard/81291.html).
- [NIST SSDF: selección de pruebas según riesgo y etapa](https://csrc.nist.gov/pubs/sp/800/218/final).

## Referencias de trabajo

Leer [testing](../../standards/testing.md) para gates y clasificación.
Aplicar [evidence-policy](../../standards/evidence-policy.md) a reportes y conclusiones.
Consultar [institutional-process](../../standards/institutional-process.md) para formularios y responsables.
Usar [engineering-sources](../../knowledge/engineering-sources.md) para fuentes y vigencia.
