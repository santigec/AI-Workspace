# Diseño: Marketing Office independiente

## Contexto

AI-Workspace registra skills por dominio y valida rutas, dependencias, evaluaciones y workflows. El nuevo dominio debe poder extraerse o reutilizarse sin depender de `tribe/` o `software-office/`.

## Decisiones

1. **Núcleo propio, proveedores externos por catálogo.** Los skills describen capacidades estables; `tools/external-tools.json` fija fuentes y revisiones evaluadas sin descargar código.
2. **Configuración por marca.** `knowledge/brand-profile.md` define el contrato de entrada. El repositorio no incluye perfiles reales ni credenciales.
3. **Aprobación antes de efectos externos.** Publicación, contacto, gasto y cambios de cuenta se mantienen fuera del flujo automático inicial.
4. **Descubrimiento mediante wrappers.** `.agents/skills/*` apunta al skill canónico; no duplica instrucciones.

## Estructura

```text
marketing-office/
├── README.md
├── agents/
├── knowledge/brand-profile.md
├── skills/{agency-role-selection,linkedin-marketing,local-lead-research,seo-operations}/
├── standards/external-tool-governance.md
├── templates/brand-profile.example.json
├── tools/external-tools.json
└── workflows/marketing-operations.md
```

## Seguridad y compatibilidad

- Sin `.env`, tokens, cookies ni identificadores de cuentas.
- Sin instalación, ejecución o llamadas a terceros en este cambio.
- Las cuatro revisiones externas quedan registradas para auditoría.
- La versión del workspace sube de `0.5.8` a `0.6.0` por el nuevo dominio.

## UML

No aplica en esta primera entrega: se incorpora una taxonomía documental y un catálogo, sin componentes ejecutables, APIs, persistencia ni flujo runtime. Si después se implementa un orquestador o servicio de publicación, deberá modelarse su secuencia y despliegue.

## Verificación

- Validador del workspace.
- Pruebas unitarias del validador.
- Validación estricta OpenSpec.
- Revisión de referencias relativas y ausencia de secretos.
