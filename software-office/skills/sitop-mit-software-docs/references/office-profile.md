# Reglas MIT para SITOP

## Autoridad y recursos

Los membretes originales se resuelven desde el manifiesto reference-manifest.json y la carpeta local .tools/sitop-mit del workspace. Ambos proceden de los archivos aportados por el usuario el 2026-10-20. Huellas y rutas de procedencia en `reference-manifest.json`. El arte es una imagen completa de pagina en el encabezado Word y contiene tanto los logos superiores como el pie grafico. Conservar sus bytes, proporcion y relaciones. No convertir el cuerpo completo a imagen ni usar servicios externos para dibujar logos internos.

Se elige vertical para informes/analisis/diseno corrientes; horizontal para tablas o diagramas que requieren anchura. En documentos mixtos usar el membrete adecuado a cada seccion, sin deformar el vertical. Los certificados tienen plantilla PPTX propia, artifact-template-sitop-mit-certificados; sus nombres/fechas/cargos son datos del ejemplo y se reemplazan con datos confirmados.

## Portada y numeracion

La primera hoja contiene titulo del documento y logos MIT del membrete, nombre de la oficina/proyecto, codigo, version, fecha y controles pertinentes. Sin numero visible. Usar titulo negro nativo, no una captura del texto. Mantener metadata y tabla de cambios en portada o preliminares cuando corresponda a la extension.

Desde la segunda hoja: encabezado con proyecto/titulo corto, codigo, version, creado/actualizado, elaborado/revisado/aprobado y estado; pie con codigo/version y campos Word PAGE y NUMPAGES. Conservar pie grafico institucional en todas las hojas. Personas, fechas de revision/aprobacion, codigo oficial y firmas pendientes si no se confirmaron. Actualizar etiquetas/estado del helper cuando el documento deje de ser borrador, solo con evidencia real.

Convencion elegida: portada cuenta como hoja fisica 1 pero se oculta su numero; la segunda muestra 2 de N. Si el usuario solicita que el cuerpo empiece en 1, preparar seccion de portada separada, ajustar NUMPAGES/SECTIONPAGES segun alcance y verificarlo. No inferir esta variante por rutina.

Diferente primera pagina solamente en la seccion inicial. Secciones posteriores conservan numeracion y controles en su primera pagina. Desactivar distincion par/impar salvo una necesidad expresa. No reiniciar w:pgNumType al insertar landscape ni vincular encabezados de orientaciones diferentes. Mantener PAGE nativo y calcular TOC contra render antes de entregar.

## Contenido y trazabilidad

Para documentos de software conservar IDs estables y relacion RF/RNF, CU con pre/post, flujo principal, alternativas y errores, SEQ por CU, diccionario cuando exista, pruebas/evidencia y version. Vincular F0-F5 por etapa conforme a AI-Workspace sin alterar etiquetas o simular aprobaciones. La identidad visual no certifica IEEE, requisitos, ejecucion ni aceptacion. Historial registra version, fecha, descripcion y responsable de revision real o pendiente. Cambios de Word aceptados vuelven a fuentes antes de regenerar.

## Geometria y verificacion

El helper parte del paquete original y adapta margenes superior 1.9 e inferior 1.25 pulgadas para control y pie, conservando dimensiones A4 y margenes laterales de la orientacion. Tipografia editorial Arial 11; encabezado 8, titulos 24/16/13. Estos valores son adaptacion editorial, no una medicion de un manual de marca. Mantener texto legible; para titulo largo usar titulo corto en encabezado y revisar tabla, no reducir texto sin criterio.

Renderizar todas las paginas con el skill documents y runtime disponible. Comprobar portada sin PAGE, paginas pares/impares con membrete/control, PAGE/NUMPAGES continuos y orientacion alternativa con su propio fondo. Verificar indice/hipervinculos, tablas, diagramas, limites de pagina y ausencia de colisiones con logos/pie. Ejecutar `--demo` solo para prueba sintetica de maquetacion: no constituye evidencia funcional o institucional. El helper se probo en cuatro hojas por cada orientacion inicial, incluido cambio a la otra. Regenerar/revisar si se altera el helper o la referencia.

## Portabilidad

La autoridad operativa es esta skill en AI-Workspace. Git transporta instrucciones, helper y hashes; los binarios MIT permanecen en .tools/sitop-mit, ignorados. Consultar resources.md para restaurarlos en otro equipo. Las skills personales de plantilla son adaptadores opcionales, no la fuente principal. No se instala automáticamente en otros equipos por publicar el repositorio.
