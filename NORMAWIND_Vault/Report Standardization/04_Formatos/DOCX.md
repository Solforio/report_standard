---
tags: [formatos, docx]
---
# DOCX (documento editable)

Generado con `render_docx.py` (python-docx). **Estilos reales de Word**: el equipo puede editar y el documento mantiene su formato.

## Ejemplos (facsímil T04 · acústico CA)
| Portada | Control de revisiones | Cuerpo |
|---|---|---|
| ![[docx_T04_p1.png]] | ![[docx_T04_p2.png]] | ![[docx_T04_p3.png]] |

Carta (T08 · respuesta a requerimiento EN):

![[docx_T08_carta_p1.png|420]]

## Especificación
- **A4**, márgenes 2,2 cm laterales; superior 2,9 cm (cabecera) e inferior 2,3 cm.
- Fuente Calibri 10,5 pt, interlineado 1,12, espacio posterior 6 pt.
- `Heading 1` 16 pt marino · `Heading 2` 13 pt marino · `Heading 3` 11 pt azul · `Caption` 9 pt cursiva gris.
- Numeración manual de secciones (`1.`, `1.1`) para que coincida entre DOCX, PDF y PPTX.
- Portada con bloque marino; **primera página sin cabecera/pie**.
- Índice: **campo TOC** (niveles 1–2). La skill lo actualiza con Word antes de entregar; si Word no está disponible, Word pedirá actualizar campos al abrir.
- Tablas: cabecera marino con texto blanco, bandas alternas, cifras alineadas a la derecha, fila de cabecera repetida si salta de página, tablas cortas no se parten.
- Figuras centradas (ancho máx. 16,6 cm, alto máx. 21 cm) con pie numerado.
- Bloques especiales: tarjetas **KPI**, **callouts** (info/aviso/ok/crítico), ficha **clave–valor**.
- Estilo **carta** (respuestas): membrete, destinatario, tabla de asunto, sin portada ni índice.

## Edición posterior
- Cambiar el texto libremente; **no** cambiar manualmente numeraciones de figuras/tablas (si se añaden, renumerar).
- Para actualizar el índice: clic derecho → *Actualizar campos* (o Ctrl+A, F9).
- Si hay que rehacer el informe, **editar el YAML y regenerar** en lugar de editar el DOCX, para no perder la sincronía con PPTX/HTML.
