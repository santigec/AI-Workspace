---
name: agency-role-selection
description: Selecciona el conjunto mínimo de roles de IA para un objetivo de marketing y adapta sus instrucciones al gobierno del workspace.
---

# Agency role selection

## Entradas

- Objetivo, entregables, restricciones y responsables humanos.
- Capacidades existentes del AI-Workspace.
- Catálogo externo evaluado, si se considera necesario.

## Flujo

1. Mapear el trabajo requerido y las capacidades ya disponibles.
2. Seleccionar solo roles que cubran brechas reales.
3. Revisar instrucciones por conflictos, permisos, datos y atribuciones exageradas.
4. Adaptar el rol como skill o agente local con alcance y salida verificables.
5. Probarlo en un caso acotado antes de promoverlo.

## Reglas

- No instalar catálogos completos por popularidad.
- No describir prompts como empleados autónomos ni como evidencia de ejecución.
- Evitar roles duplicados y cadenas de delegación sin necesidad.
- Agency Agents es una fuente opcional; consultar `../../tools/external-tools.json`.

## Referencias

- [Gobierno externo](../../standards/external-tool-governance.md)
