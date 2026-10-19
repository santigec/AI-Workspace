# Usar SDD con OpenSpec

SDD es el metodo: especificar antes de implementar y verificar contra esa especificacion. OpenSpec organiza los artefactos. AI-Workspace conserva las reglas comunes; cada producto conserva sus especificaciones junto al codigo. Gentle-AI no se instala ni se necesita para adoptar este flujo.

La exploracion estructural se apoya en [CodeGraph](codegraph.md) cuando la herramienta y el indice del producto estan disponibles. Configurar MCP y construir cada indice son pasos locales distintos de leer las reglas de AI-Workspace.

Los [modelos UML](uml.md) afectados se mantienen en la misma entrega: fuentes editables, referencias, render real y comprobacion de deriva con revision semantica/visual. Si no hay modelo afectado, dejar la razon en el cambio; no marcar documentacion actualizada por solo generar una imagen.

## En AI-Workspace

Dependencia local fijada a OpenSpec 1.14.3. Con Node compatible y npm:

```powershell
npm ci
npm run openspec -- --version
npm run openspec:check
npm run test:openspec
```

Las pruebas comprueban el CLI y las configuraciones. No son pruebas de aplicaciones Java/Angular/Django.

## Adoptar en SITOP V2 o Tribe Sport

1. Abrir el repositorio real de la aplicacion. Revisar Git, AGENTS.md, package.json/lockfiles, estructura y cualquier openspec existente; conservar lo vigente.
2. Elegir una version compatible de OpenSpec y fijarla usando el gestor ya empleado. Si el proyecto usa npm y no tiene OpenSpec, una opcion es `npm install --save-dev --save-exact @fission-ai/openspec@1.14.3`. No crear un segundo lockfile si usa otro gestor. En Django puede existir una dependencia de herramientas Node sin cambiar el backend Python; no instalar globalmente por defecto.
3. Si no existe inicializacion, ejecutar el CLI local `npx --no-install openspec init --tools codex` y revisar los archivos generados. Si ya existe, comparar y fusionar configuracion, sin usar --force de rutina. Las opciones dependen de la version instalada.
4. Fusionar el perfil de `software-office/templates/openspec/sitop-v2.config.yaml` o `tribe-sport.config.yaml` en `openspec/config.yaml` del producto. Conservar otros context/rules/esquemas existentes. Registrar la ubicacion accesible y commit de AI-Workspace en las instrucciones del producto; los wrappers de este repo dependen de sus rutas relativas.
5. Crear el primer cambio: `npx --no-install openspec new change <nombre-kebab-case>`. Consultar `status --change <nombre> --json` e `instructions <artefacto> --change <nombre>` para generar proposal, specs, design y tasks desde la version instalada. Crear el directorio no crea por si solo los cuatro artefactos terminados.
6. Implementar tareas desde escenarios; validar con `npx --no-install openspec validate --all --strict --no-interactive`, ejecutar pruebas del producto y completar el informe complementario de verificacion. Revisar antes de archivar y publicar. Tras archivar, repetir validacion de specs vigentes y tareas archivadas: al crear una capacidad, el CLI puede dejar un Purpose provisional que debe reemplazarse por su proposito real.

Los comandos de terminal y las invocaciones del chat son superficies distintas. Utilizar las invocaciones que imprima `init` para el adaptador instalado; no asumir que nombres slash de otro asistente funcionan aqui. Si el chat puede leer AI-Workspace, tambien puede usar su skill propia `sdd-openspec` explicitamente por ruta.

## Prompt de inicio o continuidad

```text
Trabaja en este repositorio con SDD y OpenSpec.
Perfil: SITOP V2 [o Tribe Sport].
AI-Workspace esta en: [ruta accesible].
Cambio: [identificador o descripcion].

Lee AGENTS.md, la politica software-office/standards/sdd-openspec.md
y el skill software-office/skills/sdd-openspec/SKILL.md de AI-Workspace.
Comprueba acceso, revision y herramientas instaladas.
Revisa primero codigo y especificaciones actuales; recupera el cambio
existente o prepara propuesta, escenarios, diseno y tareas antes de implementar.
Aplica el perfil documental correspondiente, prueba contra los escenarios
y registra evidencia real, pendientes y decisiones para continuar.
```

No hace falta repetir especificaciones en cada chat: versionar `openspec/` e instrucciones del producto, mantener memoria separada por proyecto y hacer pull/import explicitamente al cambiar de equipo. Las rutas de los repositorios reales y la instalacion en cada destino deben comprobarse; esta guia no afirma que ya esten conectados.

Referencias: [politica comun](../software-office/standards/sdd-openspec.md), [workflow](../workflows/software-office/sdd-openspec.md), [inicio oficial](https://github.com/Fission-AI/OpenSpec/blob/main/docs/getting-started.md) y [CLI oficial](https://github.com/Fission-AI/OpenSpec/blob/main/docs/cli.md).
