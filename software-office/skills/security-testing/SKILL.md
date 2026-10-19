---
name: security-testing
description: Planifica y documenta pruebas de controles de seguridad con ASVS/WSTG en entornos autorizados; no certifica seguridad ni ISO.
---

# security-testing

Evaluar controles concretos contra requisitos de seguridad y riesgo declarado.
Usar ASVS como catálogo de requisitos y WSTG como guía de técnicas, con versión e ID.
Mantener la revisión humana especializada cuando el control no admite verificación automática suficiente.

## Procedimiento

1. Confirmar alcance autorizado, sistemas, cuentas, datos, técnicas y ventana de ejecución.
2. Acordar límites de tráfico/recursos, criterios de parada, contacto y manejo de hallazgos.
3. Seleccionar controles aplicables por riesgo; justificar N/A y registrar incertidumbre.
4. Preparar casos con precondiciones, acciones, resultado esperado y evidencia saneada.
5. Preferir pruebas no disruptivas; explotación, carga o alteración de datos requieren alcance autorizado concreto.
6. Ejecutar sólo dentro de límites y detener ante impacto inesperado o salida del alcance.
7. Registrar versiones de herramientas/reglas, configuración, objeto exacto y reportes originales.
8. Revisar falsos positivos, registrar defectos reproducibles y retestar correcciones.

## Artefactos obligatorios

- Plan de seguridad con autorización referenciada, alcance, restricciones y parada.
- Matriz requisito/control versionado -> caso -> resultado y aplicabilidad justificada.
- Reportes, comandos, exit codes, logs saneados y hashes; observaciones manuales con referencia.
- Hallazgos, severidad razonada, remediación, retest y excepciones del dueño del riesgo.

## Límites

Usar ASVS 5.0.0 y WSTG 4.2 como bases verificadas; confirmar versión si el proyecto pide otra.
No confundir WSTG 5.0 en desarrollo con publicación estable.
Un escáner sin hallazgos no acredita todos los controles ni ausencia de vulnerabilidades.
No ejecutar contra producción o terceros por inferencia del objetivo general.
No incluir secretos, tokens o datos personales en artefactos compartidos.
La skill no acepta riesgo, firma por humanos ni concede certificación ISO.
Skipped/not_run y controles sin evidencia permanecen explícitos; no declararlos conformes.

## Fuentes primarias

- [OWASP ASVS y referencias versionadas](https://owasp.org/projects/asvs).
- [OWASP WSTG y versiones](https://owasp.org/projects/web-security-testing-guide).
- [NIST SSDF, PW.8](https://csrc.nist.gov/pubs/sp/800/218/final).
- [ISO: alcance de certificación](https://www.iso.org/certification.html).

## Referencias de trabajo

Leer [testing](../../standards/testing.md) para gates y clasificación.
Aplicar [evidence-policy](../../standards/evidence-policy.md) a reportes y conclusiones.
Consultar [institutional-process](../../standards/institutional-process.md) para formularios y responsables.
Usar [engineering-sources](../../knowledge/engineering-sources.md) para fuentes y vigencia.

