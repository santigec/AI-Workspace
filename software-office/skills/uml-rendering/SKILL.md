---
name: uml-rendering
description: Renderiza y verifica UML editable con PlantUML o Mermaid locales, revisa SVG y PNG y detecta diagramas desactualizados respecto de fuentes y codigo referenciado.
---

# Renderizado y vigencia de UML

Leer [estandar UML](../../standards/uml.md) y [guia de herramientas](../../../docs/uml.md). Usar modelos pertinentes a los escenarios del cambio y distinguir ejemplo, propuesta y sistema observado.

1. Identificar proyecto y fuentes existentes. Usar PlantUML para UML formal (casos de uso, clases, secuencia, actividad, estados, componentes, despliegue). Mermaid es apropiado para clases, secuencia o estados en documentacion; no sustituye tipos que no soporta ni certifica notacion UML completa.
2. Comprobar herramientas fijadas y ejecutar setup local si faltan. Usar el script central scripts/uml.py con --project y --manifest del producto; no trasladar su codigo al workspace. Renderizar localmente sin enviar modelos internos a servicios externos.
3. Crear o actualizar manifiesto con fuente editable, scope y code_refs pertinentes. Modelos observados requieren referencias verificadas; un ejemplo no acredita arquitectura de la aplicacion. Conservar IDs de requisitos y cambios OpenSpec en el modelo/documentacion.
4. Ejecutar render para producir SVG y PNG en outputs/uml y check para detectar deriva. Si cambio codigo referenciado y el modelo queda igual, inspeccionar el cambio y proporcionar --review-note con razon concreta o modificar el diagrama. No usar una nota vacia ni regeneracion mecanica como revision semantica.
5. Inspeccionar graficos reales: texto legible, etiquetas completas, flechas y relaciones distinguibles, actores/fronteras correctos, multiplicidades y alternativas coherentes. Corregir fuentes y volver a renderizar cuando haya problemas; no entregar una imagen de error como resultado valido.
6. Antes de cerrar cada cambio evaluar modelos afectados y actualizar fuente, render y revision, o registrar que no aplican. Check de hashes solo detecta deriva de dependencias declaradas; revisar las omitidas y coherencia del sistema con uml-modeling y pruebas.

Versionar fuentes, manifiestos y estado ligero; dejar JAR, runtime, navegador e imagenes generadas fuera de Git conforme a las reglas del repo. En una nueva maquina renderizar otra vez: que falten imagenes locales no indica que se deba versionar binarios.
Las herramientas no se actualizan a latest silenciosamente. Revisar versiones oficiales al planificar mantenimiento o detectar incompatibilidad, actualizar pins/checksums/lockfile y repetir pruebas/inspeccion. Mantener diagramas por cambio no implica instalar una automatizacion periodica.
