---
name: spring-security
description: Configura y revisa autenticación y autorización Spring Security para sesiones u OAuth2/JWT con pruebas de acceso.
---

# Seguridad Spring

## Alcance y entradas

Aplicar a reglas de acceso, autenticación e integración con proveedores de identidad en Spring.
Recibir clientes, rutas, identidades, permisos y mecanismo vigente; inspeccionar la configuración
real y versiones de Boot/Security antes de seleccionar DSL o dependencias.
Leer el [proceso](../../standards/institutional-process.md) y el
[estándar Java/Spring](../../standards/java-spring-boot.md).

## Acciones

1. Identificar el flujo: sesión de navegador, OAuth2 login, resource server JWT u opaque token.
   Documentar la frontera entre proveedor de identidad y aplicación; no añadir un emisor propio
   como consecuencia automática de proteger una API.
2. Construir una matriz de rutas/operaciones, actores y permisos; incluir acceso al objeto concreto
   para evitar que un usuario autorizado consulte o cambie datos de otro.
3. Mantener SecurityFilterChain y autorización coherentes con la versión del proyecto. Revisar
   reglas públicas y reglas por defecto, y explicar cualquier cambio de exposición.
4. Para JWT, obtener issuer y audience esperada de la integración real; verificar firma, algoritmo,
   expiración y nbf mediante soporte del framework. Comprobar configuración de claves/rotación
   y traducción explícita de scopes o claims a authorities; no inventar endpoints ni secretos.
5. Decidir CSRF desde el modo de autenticación y comportamiento del navegador: una API que usa
   cookies no queda exenta por llamarse REST. Definir CORS con orígenes y credenciales reales;
   CORS no sustituye autorización ni impide solicitudes de clientes ajenos al navegador.
6. Mantener credenciales fuera del repositorio y evitar registrar tokens. Cuando existan
   contraseñas locales, usar PasswordEncoder apropiado y conservar una estrategia de migración.
7. Probar acceso permitido, anónimo, permiso insuficiente y acceso a objeto ajeno. Para JWT,
   distinguir pruebas con identidad simulada de pruebas reales del decoder y sus validadores.
8. Ejecutar pruebas relevantes; comprobar semántica 401/403, sesión/logout o expiración según
   el flujo y explicar dependencias del proveedor que no se pudieron comprobar.

## Evidencia de salida

- Modelo de autenticación y matriz de autorización, cambios de configuración y sus motivos.
- Casos negativos/positivos ejecutados y alcance real de la validación de tokens.
- Información de integración faltante y puntos de operación: claves, secretos o proveedor.

## Límites

No desactivar CSRF, abrir CORS o permitir todas las rutas para silenciar errores de integración.
No reemplazar validación criptográfica por lectura de claims ni generar filtros JWT caseros por defecto.
El skill no autoriza rotar credenciales reales, publicar secretos o cambiar cuentas externas.

## Referencias

[Catálogo y procedencia](../../knowledge/engineering-sources.md).
- [Resource Server JWT](https://docs.spring.io/spring-security/reference/servlet/oauth2/resource-server/jwt.html).
- [CSRF](https://docs.spring.io/spring-security/reference/servlet/exploits/csrf.html).
- [CORS](https://docs.spring.io/spring-security/reference/servlet/integrations/cors.html).
- [Autorización de solicitudes](https://docs.spring.io/spring-security/reference/servlet/authorization/authorize-http-requests.html).
