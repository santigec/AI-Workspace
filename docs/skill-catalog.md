# Catálogo — 21 skills

Todos están en estado **alpha**. Los wrappers de .agents/skills son entradas de descubrimiento, no skills adicionales. La referencia de versiones es registry/skills.yaml; leer el SKILL.md correspondiente antes de ejecutar.

| Skill | Dominio | Características relevantes |
|---|---|---|
| image-analysis | shared | Analiza composición, texto, fondo y restricciones de referencias antes de editar. |
| research | shared | Investiga y respalda conclusiones con fuentes verificables. |
| professional-writing | shared | Redacción y revisión según audiencia, propósito y tono. |
| presentation | shared | Narrativa, mensajes y evidencias para presentaciones. |
| image-generation | image-studio | Arte nuevo desde brief y referencias; requiere herramienta de generación disponible. |
| image-editing | image-studio | Cambios sobre imagen existente conservando los elementos indicados. |
| preserve-original-art | image-studio | Adaptación con prioridad de fidelidad al arte original. |
| resize-to-print | image-studio | Ajuste a medidas físicas y resolución confirmadas; no inventa detalle original. |
| transparent-png | image-studio | Sujeto recortado o fondo eliminado con transparencia real. |
| print-ready-qa | image-studio | QA de archivos reales contra especificaciones de impresión; no basta un pedido válido. |
| sublimation-layout | tribe | Composición de sublimación sobre el área imprimible confirmada del producto. |
| dtf-layout | tribe | Organización de arte para DTF según requisitos del proveedor. |
| product-specs | tribe | Recopilación/verificación de medidas y requisitos de producción. |
| mug-sublimation | tribe | Taza 205×95 mm, arte plano, referencia opcional y fondo transparente/blanco/temático según pedido. |
| tumbler-sublimation | tribe | Flujo común por capacidad; 500 ml 232×125 mm, 600 ml 232×142 mm, 750 ml 232×182 mm. Arte plano continuo. |
| tumbler-600ml-sublimation | tribe | Entrada específica 600 ml, 232×142 mm; conserva las reglas comunes de tomatodos. |
| tumbler-750ml-sublimation | tribe | Entrada específica 750 ml, 232×182 mm; conserva las reglas comunes de tomatodos. |
| agenda-design | tribe | Nueve modelos A4 vertical más etiquetas 205×165/205×95 mm. Interiores blancos profesionales; datos en blanco; calendarios exactos; cuadrícula con cabecera ilustrada, lettering temático y marca de agua; portadas sin Agenda por defecto. |
| sql-review | software-office | Revisión de lógica SQL, rendimiento y efectos sobre datos. |
| system-design | software-office | Diseño de sistemas desde requisitos y restricciones explícitas. |
| technical-presentation | software-office | Presentación de propuestas técnicas para decisión o transferencia de conocimiento. |

Invocación en Codex: `$nombre-del-skill`. Disponibilidad y ejecución dependen de las herramientas de la sesión. Los formatos y reglas se transfieren con el repo; la memoria Engram conserva los motivos y correcciones.
