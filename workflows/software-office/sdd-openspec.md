# Desarrollo con SDD y OpenSpec

Entrada: solicitud autorizada, repositorio objetivo y perfil SITOP V2 o Tribe Sport.

1. **Explorar.** sdd-openspec identifica codigo, contratos y especificaciones actuales; research se usa solo para informacion externa necesaria. Recuperar memoria pertinente sin reemplazar evidencia del repo.
2. **Especificar.** sdd-openspec prepara propuesta, deltas con escenarios y criterios, diseno proporcional y tareas trazables. system-design apoya arquitectura y diagramas cuando el cambio lo amerita.
3. **Aplicar.** Implementar tareas usando el stack del producto. No iniciar codigo funcional sobre supuestos pendientes ni cambiar especificacion retrospectivamente para ocultar un fallo.
4. **Verificar.** Validar OpenSpec y ejecutar pruebas relevantes del codigo; distinguir estructura, comportamiento, revision y aceptacion. Registrar fallos y omisiones; las tareas de pruebas no terminan por existir un archivo de plan.
5. **Cerrar.** Revisar y archivar/consolidar especificaciones, guardar conocimiento y publicar lo autorizado. technical-presentation se usa si se solicita una entrega comunicacional; no es una aprobacion de desarrollo.

SITOP V2 conserva Java/Spring Boot + Angular y F0-F5. Tribe Sport conserva Python/Django + Railway y documentacion ligera. Diagramas, contratos y evidencia se dimensionan al riesgo; ambos perfiles comparten especificaciones verificables antes de implementar.

No hay activacion automatica de agentes por escribir el nombre de esta politica. Los roles deben estar disponibles o cargarse explicitamente con autorizacion; un skill no equivale a un perfil TOML.
