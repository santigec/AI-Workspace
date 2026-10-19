# RESPONSABILIDAD DE PASO A PRODUCCIÓN

Formulario F5. Representación Markdown vacía de los campos originales. Sin firmas ni aprobaciones emitidas. La maquetación del original no ha sido validada mediante render. [Proceso y límites](../../standards/institutional-process.md).

## 1.- DATOS

### Información

| Campo | Valor |
|---|---|
| ID: | |
| Fecha: | |
| Ticket asociado: | |
| Sistema: | |
| Ambiente: | |
| Asunto: | |

Emergente:

- [ ] SI
- [ ] NO

Guías del original: ID MTOP-UDSI-PAP-xxx; fecha Año-mes-día; ticket Número GLPI. No se preseleccionan opciones ni ambiente.

## 2.- REQUERIMIENTO

| Nombre | Detalle |
|---|---|
| URL/IP: | |
| Nombre del módulo/BDD/Tabla: | |
| Detalle: | |
| Ambiente a instalar: | |

## 3.- PREREQUISITOS

Responsable: Analista de Infraestructura:

La fuente exige respaldar el componente alojado en servidor identificando su ruta. Detallar el respaldo del caso en el espacio siguiente.


## 4.- PROCEDIMIENTO PASO A PRODUCCIÓN

Responsable: Analista de Infraestructura

La aplicación del paso a producción en ambientes productivos, deberá generarse fuera de horario laboral; excepto para cambios emergente que deberán ser expresamente autorizados por la Dirección de Tecnologías de la Información. De ser necesario se deberá gestionar la correspondiente ventana de mantenimiento.



## 5.- PROCEDIMIENTO ROLLBACK

Responsable: Analista de Infraestructura:

En caso de que se generarán errores durante el proceso de paso a producción se deberá proceder con el Rollback, de acuerdo al siguiente detalle:

1. Reemplazar el último respaldo de producción con el anterior vigente, respaldado antes del cambio.
2. Verificar si la aplicación se encuentra operativa.

Espacio para detalle del caso:



## 6.- PROCEDIMIENTO DE VERIFICACIÓN

Responsable: Administrador de la aplicación:

Ingresar al navegador y validar el acceso de los siguientes URLs:



## 7.- AUTORIZACIÓN PARA SUBIR A PRODUCCIÓN

| Responsables | Cargo: | Nombre: | Firma: |
|---|---|---|---|
| SOLICITADO POR: | | | |
| REVISADO POR: | | | |
| APROBADO POR: | | | |

## 8.- EJECUCIÓN DE PASO A PRODUCCIÓN:

| Responsable | Cargo | Nombre | Firma |
|---|---|---|---|
| ELABORADO POR: | | | |

El texto fuente se obtuvo directamente del DOC binario y se cotejó con PDF auxiliar. No se certifica geometría ni representación de casillas. Versión/tag/hash del artefacto, migraciones y pruebas de rollback se adjuntan como complementos técnicos identificados. Esta plantilla y el baseline no autorizan una ejecución en producción. Aplicar [política de evidencia](../../standards/evidence-policy.md).
