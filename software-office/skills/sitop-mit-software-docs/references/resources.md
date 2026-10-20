# Recursos locales y uso en otros equipos

Resolver la raíz de AI-Workspace desde la ubicación de esta skill, sin fijar unidad F: o usuario. El manifiesto reference-manifest.json contiene rutas relativas y SHA256 de los dos originales aportados. En este equipo ambos están en .tools/sitop-mit. El helper usa Python con python-docx; el render requiere las herramientas de documentos disponibles (por ejemplo LibreOffice y Poppler). Comprobar disponibilidad; no descargar o instalar componentes globales por inferencia.

En otro equipo: clonar/actualizar develop; importar Engram del proyecto ai-workspace; restaurar los dos archivos originales autorizados bajo las rutas del manifiesto y comprobar SHA256. El nombre original no sustituye esta verificación. Si faltan, solicitar el recurso o documentar que la generación con marca está pendiente. No copiar salidas de otro producto como base de contenido. Los binarios no se publican en Git.

Uso del helper desde Python: importar scripts/sitop_mit_template.py, llamar new_document(reference, title, code, version, created=..., prepared=..., reviewed=..., approved=...) y añadir contenido después de la portada creada. add_orientation(doc, other_reference, metadata) añade la orientación alternativa sin reiniciar números. Guardar en una salida distinta del original. No usar --demo como contenido entregable: solo produce datos sintéticos para revisar maquetación.

Esta skill puede consumirse leyendo su SKILL.md desde el checkout. El acceso .agents/skills/sitop-mit-software-docs sirve dentro de AI-Workspace; otro proyecto debe referenciar explícitamente la skill central o instalar un paquete completo conservando sus referencias. Publicar Git no configura descubrimiento global en Codex.
