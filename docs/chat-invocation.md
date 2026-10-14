# Usar mug-sublimation desde otro chat

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
Si no hay referencias, genera arte nuevo con la descripción. Si debe conservarse un original, adjúntalo.

## Invocación corta con skill descubierto

```text
$mug-sublimation
Taza 205 × 95 mm para Sebastián, dinosaurios infantiles.
Fondo temático de selva como la referencia adjunta.
PNG con fondo, plano y continuo. Genera y muestra el diseño.
```

Si el skill no aparece o el chat no puede leer el repositorio, usa el prompt portable y proporciona los archivos y referencias necesarios. Un enlace privado por sí solo no garantiza acceso.
