# Expediente reutilizable

## Análisis

Propósito, alcance, actores, contexto, fuentes y limitaciones. RF/RNF con IDs y criterios verificables; usar estructura inspirada en IEEE 830 cuando sea pertinente, sin reproducir la norma ni afirmar certificación. Separar restricciones observadas de objetivos propuestos. Cada CU: actor, objetivo, pre/postcondiciones, principal, alternativas, validaciones/errores y RF relacionados. Las mejoras propuestas se distinguen explícitamente.

## Diseño

Arquitectura, componentes, dependencias/versiones, entradas/salidas, contratos/archivos, ejecución/build y limitaciones. UML proporcional y secuencia obligatoria por CU incluido en el expediente; referencia bidireccional CU ↔ SEQ. Diccionario: entidad/campo, tipo, origen, validación, uso/salida y sensibilidad cuando aplique; no inventar base de datos. Describir aspectos importantes del flujo sin copiar todo el código. Gráficos locales legibles, con ID, título y fuente editable.

## Proceso e impacto

Matriz RF/RNF ↔ CU ↔ SEQ ↔ dato/contrato ↔ implementación ↔ CP ↔ evidencia/versión. Enlazar F0 solicitud, F1 requisitos, F2 estimación, F3 plan QA, F4 aceptación y F5 producción según etapa. Mantener etiquetas originales del baseline institucional, datos pendientes explícitos y roles/códigos distintos. El expediente técnico complementa los formularios; no equivale a su emisión ni conserva geometría oficial por solo reutilizar sus etiquetas.

Ante un cambio: identificar IDs/documentos afectados; actualizar primero especificación/diseño; después código/pruebas y evidencia; actualizar UML o justificar no afectación concreta; regenerar documentos e índices. No marcar CP como PASS sin ejecución ni F4/F5 como aprobados por un build. Si solo cambia presentación, verificar preservación del contenido y fuentes funcionales.

## Fuentes y continuidad

Usar catálogo/perfil/generador por producto cuando exista; no copiar el generador específico de SPI como si fuera universal. Registrar fuentes, revisión consumida de AI-Workspace, comandos y versiones de herramientas. Evidencia mínima de pruebas: versión/hash, entorno, entrada sintética, esperado, obtenido, estado, fecha y responsable real. Mantener estado de continuidad con pendientes y primera prueba ejecutable.
