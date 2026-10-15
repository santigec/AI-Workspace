# Usar mug-sublimation desde otro chat

## Tomatodo 750 ml

```text
$tumbler-750ml-sublimation
Tomatodo 750 ml: 232 mm de ancho × 182 mm de alto.
Temática y texto: [indicar].
Fondo: [blanco / transparente / temático].
Usa las referencias adjuntas si las hay.
Genera y muestra arte plano y continuo para impresión y sublimación.
Adapta la composición a toda la superficie sin estirar el dibujo.
Entrega el PNG descargable.
```

La entrada selecciona producto tumbler_750ml y workflow común tumbler-sublimation. Requiere el repositorio accesible o el skill instalado.

## Tomatodo 600 ml

Para 600 ml, usa la entrada específica:

```text
$tumbler-600ml-sublimation
Tomatodo 600 ml: 232 mm de ancho × 142 mm de alto.
Temática y texto: [indicar].
Fondo: [blanco / transparente / temático].
Usa las referencias adjuntas. Genera y muestra arte plano y continuo,
adaptado a esta altura sin deformaciones, listo para revisar y descargar.
```

El skill de entrada es tumbler-600ml-sublimation; la orden usa workflow tumbler-sublimation y producto tumbler_600ml.

## Tomatodo 500 ml

Usa tribe/skills/tumbler-sublimation/SKILL.md y sus referencias. En Codex con el checkout accesible:

```text
$tumbler-sublimation
Tomatodo de 500 ml: 232 mm de ancho × 125 mm de alto.
Temática y texto: [indicar].
Fondo: [blanco / transparente / temático y descripción].
Usa las imágenes adjuntas como referencias si las hay.
Genera y muestra arte plano, continuo y horizontal para impresión y sublimación.
Adapta la composición al espacio sin deformar elementos y entrega PNG descargable.
```

El skill tiene entrada de descubrimiento en .agents/skills/tumbler-sublimation. ChatGPT requiere el skill instalado o los archivos accesibles; escribir el nombre no lo instala.

## Con el repositorio accesible

Abre o conecta AI-Workspace y selecciona develop. Para reproducir una versión, usa el commit indicado en lugar de depender de la punta de una rama.
El punto de entrada de Codex vive en .agents/skills/mug-sublimation/SKILL.md; la definición de dominio está en tribe/skills/mug-sublimation/SKILL.md.
La [documentación oficial](https://learn.chatgpt.com/docs/build-skills) explica descubrimiento desde .agents/skills e invocación explícita con $ en Codex CLI/IDE y @ en ChatGPT cuando el skill esté disponible.
Guardar un repo privado en GitHub no lo conecta ni instala automáticamente en otro chat.

## Prompt portable

```text
Usa el repositorio santigec/AI-Workspace, rama develop.
Lee tribe/skills/mug-sublimation/SKILL.md y sus referencias.

Genera y muéstrame el diseño de una taza:
- Nombre exacto: Sebastián
- Temática: dinosaurios
- Estilo: infantil, profesional y limpio
- Lienzo: 205 mm de ancho × 95 mm de alto
- Fondo: temático, paisaje de selva con cielo y vegetación
- Salida: PNG con fondo opaco, arte plano y continuo

Usa las imágenes adjuntas como referencias de estilo y fondo.
Si adjunto un diseño existente, conserva nombre, personajes y composición principal al añadir el fondo.
Mantén dimensiones y proporciones; entrega imagen visible y archivo descargable.
Indica los datos de producción que falten sin impedir un borrador útil.
```

Para transparencia cambia Fondo a transparente; para color uniforme usa sólido y describe el color.
Para superficie blanca escribe: "Lienzo blanco opaco de 205 × 95 mm; conserva los fondos internos del dibujo y elimina la ficha y precio de la captura". Esto se modela como background solid con background_description "Lienzo blanco opaco".
Para aprovechar el ancho de la taza añade: "Adapta la composición completa al formato horizontal; redistribuye texto e ilustración sin estirarlos. No centres un póster vertical dejando grandes vacíos laterales".
Si no hay referencias, genera arte nuevo con la descripción. Si debe conservarse un original, adjúntalo.

## Invocación corta con skill descubierto

```text
$mug-sublimation
Taza 205 × 95 mm para Sebastián, dinosaurios infantiles.
Fondo temático de selva como la referencia adjunta.
PNG con fondo, plano y continuo. Genera y muestra el diseño.
```

Si el skill no aparece o el chat no puede leer el repositorio, usa el prompt portable y proporciona los archivos y referencias necesarios. Un enlace privado por sí solo no garantiza acceso.
