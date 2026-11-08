# marketing-office Specification

## Purpose
Definir una oficina portable de marketing que separe capacidades reutilizables, configuración de marca e integraciones externas, con aprobación humana antes de cualquier efecto externo.

## Requirements

### Requirement: MKT-001 Oficina independiente

AI-Workspace MUST mantener `marketing-office` como dominio independiente de Software y Tribe. Sus skills MUST operar con un perfil de marca suministrado y MUST NOT incorporar valores de una marca como comportamiento predeterminado.

#### Scenario: Reutilizar la oficina
- **WHEN** un proyecto nuevo consume un skill de marketing
- **THEN** proporciona su propio perfil de marca
- **AND** no hereda identidad, cuentas ni contenido de otro proyecto

#### Scenario: Perfil ausente
- **WHEN** una tarea requiere voz, audiencia o canales y no existe perfil suficiente
- **THEN** el skill MUST solicitar únicamente los datos faltantes
- **AND** MUST NOT inventar decisiones de marca

### Requirement: MKT-002 Aprobación y permisos

Los skills MUST preparar borradores y análisis sin publicar, contactar prospectos, gastar créditos ni modificar cuentas hasta recibir autorización explícita para esa acción. Las credenciales MUST permanecer fuera del repositorio.

#### Scenario: Publicación solicitada sin conexión aprobada
- **WHEN** un skill produce contenido pero no existe una integración autorizada
- **THEN** entrega un borrador listo para revisión
- **AND** informa que la publicación permanece NOT_RUN

#### Scenario: Acción con costo o datos personales
- **WHEN** una herramienta requiere pago, scraping o tratamiento de datos personales
- **THEN** el flujo MUST exponer costo, finalidad y restricciones antes de ejecutar

### Requirement: MKT-003 Adaptadores reemplazables

Las herramientas externas MUST registrarse con fuente, licencia, revisión evaluada, función, dependencias y riesgos. Un skill MUST describir la capacidad de negocio sin depender de que un proveedor específico esté instalado.

#### Scenario: Proveedor no disponible
- **WHEN** la herramienta externa no está instalada o conectada
- **THEN** el skill conserva el análisis o borrador posible
- **AND** identifica la capacidad que quedó NOT_RUN

#### Scenario: Actualización externa
- **WHEN** se propone cambiar la revisión evaluada
- **THEN** se revisan licencia, permisos, costos, comportamiento y pruebas antes de actualizar el catálogo

### Requirement: MKT-004 Prospección responsable

La investigación de prospectos MUST limitarse a un propósito empresarial definido, minimizar los datos recopilados y separar investigación de contacto. El sistema MUST NOT asumir que un dato público autoriza mensajes masivos.

#### Scenario: Lista de negocios locales
- **WHEN** se investiga un segmento y una ubicación
- **THEN** se registra la fuente y se recopilan solo los campos necesarios
- **AND** cualquier contacto posterior requiere una decisión separada

