# Primera prueba del equipo operativo — 2026-10-19

## Alcance y ejecución

Petición del usuario: definir y probar coordinador, diseñador y revisor. Prueba elegida: revisión sin cambios de una sola hoja cuadriculada K-pop existente. Sin generación nueva ni archivos pesados añadidos a Git.

Tres delegaciones reales y secuenciales desde el hilo principal, con los perfiles TOML cargados explícitamente en sus encargos:

| Etapa | Rol | Resultado observado |
|---|---|---|
| RECIBIDO | coordinador | Leyó reglas y continuidad, confirmó existencia de archivos y entregó brief/aceptación delimitados. |
| EN_DISENO | disenador | Abrió preview, PDF y metadatos; devolvió evidencia de medidas y composición sin editar. |
| EN_REVISION | revisor | Abrió y renderizó PDF independientemente, contrastó preview e informe; PASS digital sin correcciones obligatorias. |
| ENTREGADO | principal/coordinación | Consolidó resultados y limitaciones; persistió solo conocimiento y perfiles. |

Arte local inspeccionado: `design-runs/agenda-kpop-2026-10-15-v2/entrega/09-hoja-cuadriculada.pdf` y su `detalle-09-hoja-cuadriculada.png`. Estos archivos están ignorados y no viajan al segundo equipo por Git. El informe conserva evidencia de esta ejecución; para repetirla hacen falta un archivo equivalente disponible o esos recursos locales.

## Evidencia independiente del revisor

- PDF: una página A4 vertical, 210,000×297,000 mm.
- Área de cuadrícula: 160×195 mm; 33 líneas verticales y 40 horizontales, separaciones 4,999990–5,000025 mm (redondeo insignificante).
- Cabecera: lettering HUNTR/X con carácter/volumen, tres personajes integrados, cintas, destellos y motivos musicales. Pie coordinado y acentos laterales.
- Escritura: base blanca, líneas regulares y marca de agua central reconocible al 6% (`/ca=0.06`).
- Visual: sin títulos funcionales, Agenda, Tema/Fecha ni nombre personal; sin defectos visibles o recortes detectados. Sin texto extraíble: los textos del emblema se comprobaron visualmente.
- PNG final: 2481×3508 px, metadatos 299,9994 ppp. Cabecera original incrustada 2172×724 px, 285,11 ppp efectivos. Preview 893×1263 px, composición coincidente.

## Resultado y límites

**PASS de coordinación y revisión digital de esta pieza**, sin necesidad de ronda de corrección. No se certifica el conjunto completo ni PRINT_READY. Prueba física, encuadernación y otras diez piezas: NOT_VERIFIED. Los casos formales de evaluación de skills que estaban NOT_RUN mantienen su estado; este informe no los promociona ni cambia el número de skills.

Los tres TOML se analizaron con tomllib y contienen name/description/developer_instructions, sin imponer modelo/permisos. Las 43 pruebas técnicas existentes pasaron. Validación de estructura del workspace: PASS.

**Descubrimiento nativo automático de perfiles: NOT_VERIFIED.** Los roles se probaron mediante delegaciones que leyeron los perfiles por ruta; puede requerirse un chat nuevo para comprobar su descubrimiento nativo.

## Aprendizaje

El coordinador intentó consultar Engram desde el sandbox del subagente y encontró bloqueo del lock local; usó continuidad y reglas versionadas sin fingir recuperación. El hilo principal había importado la memoria correctamente. Se ajustó el perfil: si el padre ya recuperó memoria, pasarla en el brief sin duplicar la apertura de SQLite. Diseñador y revisor trabajaron con ese contexto y evidencia directa.
