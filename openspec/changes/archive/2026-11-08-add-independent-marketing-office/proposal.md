# Propuesta: Agregar una oficina de marketing independiente

## Intención

Incorporar capacidades reutilizables de marketing al AI-Workspace sin acoplarlas a Software, Tribe ni a un proveedor externo. La oficina debe gobernar estrategia, marca, SEO, LinkedIn, investigación de prospectos y selección de agentes con aprobación humana.

## Alcance

### Incluido
- Crear el dominio `marketing-office` con estructura portable.
- Registrar cuatro skills y un workflow inicial.
- Catalogar y fijar las revisiones evaluadas de cuatro proyectos externos sin instalar su código.
- Añadir guardas de privacidad, credenciales, costos, publicación y atribución.

### Excluido
- Conectar cuentas, almacenar credenciales o publicar contenido.
- Clonar o redistribuir repositorios externos.
- Ejecutar scraping, campañas, correos fríos o servicios pagos.
- Crear perfiles específicos de Software o Tribe.

## Capacidades

### Capacidades nuevas
- `marketing-office`: oficina portable, perfiles de marca separados, adapters externos y aprobación humana.

### Capacidades modificadas
- Ninguna.

## Enfoque

Crear skills canónicos propios que referencien herramientas externas mediante un catálogo versionado. Las marcas consumirán la oficina mediante perfiles fuera del núcleo reutilizable.

## Áreas afectadas

| Área | Impacto | Descripción |
|---|---|---|
| `marketing-office/` | Nueva | Skills, estándares, conocimiento, workflow y catálogo |
| `registry/skills.yaml` | Modificada | Dominio, skills, workflow y versión |
| `scripts/validate_workspace.py` | Modificada | Reconocimiento del dominio |
| `.agents/skills/` | Nueva | Entradas de descubrimiento |
| `evals/` | Nueva | Casos lógicos iniciales |

## Riesgos

| Riesgo | Probabilidad | Mitigación |
|---|---|---|
| Automatización no autorizada | Media | Aprobación antes de publicar o contactar |
| Dependencia o costo externo | Media | Catálogo explícito y adaptadores reemplazables |
| Datos personales o scraping indebido | Media | Minimización, propósito legítimo y revisión normativa |

## Plan de reversión

Retirar las entradas del registro y el dominio del validador; eliminar únicamente los archivos nuevos de `marketing-office`, wrappers y evaluaciones.

## Dependencias

- Ninguna dependencia externa se instala en este cambio.

## Criterios de éxito

- [ ] El workspace valida con `marketing-office` como dominio.
- [ ] Los cuatro skills son independientes de marcas y proveedores.
- [ ] Las pruebas existentes y nuevas pasan.
