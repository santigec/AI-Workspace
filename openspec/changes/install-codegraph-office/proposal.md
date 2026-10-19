## Why

El usuario solicita instalar CodeGraph como parte de AI-Workspace para mejorar la exploracion de los proyectos de software y reducir lecturas repetidas de codigo. Debe funcionar en este equipo, ser reproducible en otro y conservar solo conocimiento ligero en Git.

## What Changes

- Fijar la variante @colbymchenry/codegraph integrada por Gentle-AI como dependencia local de herramientas.
- Configurar Codex para usar su MCP y verificar realmente el protocolo y una consulta estructural.
- Incorporar skill, politica y guia que mantengan alcance, frescura del indice y lecturas acotadas.
- Excluir indices/bases locales; conservar memoria y configuracion reproducible sin prometer un porcentaje de ahorro.

## Capabilities

### New Capabilities
- `codegraph-navigation`: Exploracion estructural local de codigo para las oficinas de software.

### Modified Capabilities
- `software-sdd`: La exploracion previa a especificar o implementar usa CodeGraph cuando aporta contexto y el indice esta disponible.

## Impact

Dependencia y lockfile del workspace, herramientas/documentacion, instrucciones y entrada MCP de Codex. No instala Gentle-AI ni modifica el codigo de aplicaciones externas. Inicializa el indice de AI-Workspace; cada aplicacion requiere su propio indice local. No exporta bases o codigo a servicios remotos como parte de esta integracion.
