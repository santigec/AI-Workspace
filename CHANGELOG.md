# Historial

## 0.3.2 — Identidad temática de agendas (develop)

- agenda-design 0.1.2: cuadrícula con cabecera/pie temáticos y nombre solicitado, sin títulos informativos ni campos por defecto.
- Calendarios titulados «Calendario» y año; portadas sin «Agenda», año o eslóganes salvo petición explícita.
- Etiquetas más vivas y con estilo adaptado al tema/referencia, sin inferir género por el nombre.

## 0.3.1 — Composición profesional de interiores de agenda (develop)

- agenda-design 0.1.1: exige jerarquía editorial, módulos útiles y presencia temática proporcionada en los interiores blancos.
- Datos agrupados, meses delimitados, prioridades/seguimiento y reversos con función propia como pautas adaptables.
- QA individual a tamaño real además de la vista del conjunto; bajo consumo de tinta no implica páginas vacías.

## 0.3.0 — Agendas temáticas A4 (develop)

- agenda-design 0.1.0: nueve modelos A4 vertical y dos etiquetas de 205 × 165 y 205 × 95 mm.
- Portadas, reversos interiores, datos importantes, calendarios de dos años, actividades con líneas/columnas y cuadrícula con marca de agua central.
- Interiores blancos de bajo consumo, cabeceras/pies y acentos acordes a la temática, tipografía y personalización coherentes.
- Schema y ejemplo de pedido; planificador con calendarios calculados y años configurables, sin generar artefactos visuales.
- Pruebas de fechas, años bisiestos, formatos y política de tinta; evaluaciones visuales pendientes.

## 0.2.7 — Entrada tomatodo 750 ml (develop)

- Skill tumbler-750ml-sublimation 0.1.0: lienzo plano y continuo de 232 × 182 mm.
- Reglas comunes de tomatodos 0.1.2 distinguen 500, 600 y 750 ml y adaptan la composición a cada proporción.
- Catálogo, ejemplo, entrada de Codex y caso visual pendiente para 750 ml.
- Pruebas de selección de altura para las tres capacidades y conservación de tamaño al cambiar fondo.

## 0.2.6 — Entrada tomatodo 600 ml (develop)

- Skill tumbler-600ml-sublimation 0.1.0: arte plano y continuo de 232 × 142 mm.
- Reglas comunes tumbler-sublimation 0.1.1 resuelven dimensiones por capacidad; 500 ml conserva 232 × 125 mm.
- Catálogo y ejemplo explícitos para 600 ml, con comprobaciones de fondo, dimensiones y diferenciación de capacidad.

## 0.2.5 — Tomatodo 500 ml (develop)

- Skill tumbler-sublimation 0.1.0 con entrada de Codex y lienzo 232 × 125 mm confirmado por el usuario.
- Composición plana y continua adaptada al espacio del tomatodo, referencias opcionales y fondo configurable.
- Ejemplo estructurado de 500 ml y casos de evaluación de capacidad, tamaño y redistribución.
- No se extrapola la confirmación de dimensiones a otros parámetros de producción ni a todas las capacidades.

## 0.2.4 — Composición horizontal para taza (develop)

- mug-sublimation 0.1.2 diferencia tamaño del lienzo y adaptación de la composición.
- Referencias verticales se redistribuyen para aprovechar el ancho cuando el pedido permite adaptación; se preservan proporciones.
- Superficie blanca define la base, no exige grandes vacíos laterales.

## 0.2.3 — Superficie blanca (develop)

- mug-sublimation 0.1.1 interpreta superficie blanca como lienzo opaco del tamaño solicitado.
- Diferencia fondo blanco del archivo y sustrato físico blanco.
- Preserva fondos internos del arte y elimina elementos de captura comercial.
- Evita arrastrar nombres de pedidos anteriores a un nuevo diseño.

## 0.2.2 — Chat mug design (develop)

- Nuevo skill mug-sublimation 0.1.0 y punto de entrada de Codex en .agents/skills.
- Fondos themed con descripción y referencias de contenido, estilo o fondo desde el chat.
- Ejemplo de pedido con fondo temático, guía de invocación desde otro chat y cuatro pruebas nuevas.
- PNG admite fondo transparente u opaco; las dimensiones físicas permanecen independientes del fondo.
- Archivos de diseños reales conservados fuera del repositorio.

## Prueba lógica de pedido — 2026-10-14 (develop)

- Registrado mug-order-intake-001 sobre la base 0.2.1: orden, producto y workflow resueltos; borrador permitido y producción incompleta rechazada.
- Evidencia sin datos operativos de cliente; orden y ficha completas conservadas fuera del repositorio.
- Las pruebas lógicas por sí solas no habilitan promoción beta/stable.
- Generación, layout y QA visual siguen NOT_RUN.

## 0.2.1 — Tribe orders foundation (develop)

- Catálogos de tazas, tomatodos, camisetas, stickers y agendas: cuatro variantes propuestas y tres registros pendientes.
- Schema de producto y pedido; ejemplos sintéticos de taza y tomatodo.
- Principios de diseño y política de resiliencia con separación entre borrador y producción.
- Workflows de mug-sublimation, tumbler-sublimation y dtf-shirt.
- product-specs 0.2.1 consulta el catálogo y conserva su estado alpha.
- Validación JSON Schema y de consistencia de pedidos; producción requiere catálogo verificado y commit coincidente.
- No se crea design-runner ni se declara generación o QA de arte.

## 0.2.0 — Evaluation foundation (develop)

- Registro de 16 skills con versión, propietario, estado alpha y relaciones entre etapas.
- Contratos para image-analysis, sublimation-layout y print-ready-qa.
- 12 escenarios de evaluación NOT_RUN, incluyendo casos de sql-review.
- Workflows de sublimación, edición de imagen y diseño de sistemas con etapas condicionales.
- Guías de contratos y evaluación; validador sin dependencias externas y pruebas de regresión.
- No se declara validación de producción ni se incorpora un router ejecutable.

## 0.1.0

- Estructura de Shared, Tribe, Image Studio y Software Office.
- 16 skills iniciales con procedimientos y criterios de salida.
- Estándares comunes, ficha de producto e informe de QA.
- Agentes y herramientas reservados para fases posteriores.
