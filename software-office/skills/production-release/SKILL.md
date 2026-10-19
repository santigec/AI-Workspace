---
name: production-release
description: Preparar y revisar expediente institucional F5 de paso a producción con respaldo, instalación, rollback, verificación, horario y autorización real.
---

# Preparación de paso a producción

Alcance: preparar y revisar una liberación institucional; ejecutar solo si la acción concreta ya está autorizada. Entrada: versión candidata aceptada, ticket/cambio, ambientes y responsables confirmados.

Leer [proceso institucional](../../standards/institutional-process.md), [baseline F5](../../knowledge/institutional-forms.json) y [política de evidencia](../../standards/evidence-policy.md). Usar [F5 paso a producción](../../templates/forms/05-production-release.md).

1. Identificar ID, fecha, ticket, condición emergente, sistema, ambiente, asunto, URL/IP y módulo/BDD/tabla.
2. Con Infraestructura, precisar precondiciones, respaldo y ruta, procedimiento secuencial y rollback. El administrador de la aplicación define verificación por URLs y evidencia operativa.
3. Aplicar el control original: “La aplicación del paso a producción en ambientes productivos, deberá generarse fuera de horario laboral; excepto para cambios emergente que deberán ser expresamente autorizados por la Dirección de Tecnologías de la Información. De ser necesario se deberá gestionar la correspondiente ventana de mantenimiento.”
4. Registrar solicitado/revisado/aprobado con cargo/nombre/firma y ejecución elaborado por con responsable/cargo/nombre/firma únicamente desde hechos confirmados. Ante errores, el original requiere recuperar el respaldo anterior vigente y verificar operación.
5. Entregar plan revisable y evidencia aplicable; versión/tag/hash del artefacto, migraciones y prueba de recuperación son complementos técnicos identificados.

No confundir preparación del baseline con autorización para desplegar ahora. No producir firmas, inferir autorización de una casilla o aceptación F4, ni ejecutar si faltan autorizaciones aplicables. Si una autorización concreta sigue pendiente, completar toda preparación independiente y señalar la decisión pendiente. El texto original DOC se extrajo directamente y se cotejó con PDF auxiliar; la maquetación no está validada.
