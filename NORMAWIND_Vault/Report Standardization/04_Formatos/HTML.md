---
tags: [formatos, html]
---
# HTML (informe web autónomo)

Generado con `render_html.py`. **Un solo archivo** con CSS e imágenes incrustadas: funciona sin conexión, se envía por correo y se puede imprimir a PDF desde el navegador (hoja de estilos de impresión A4).

## Características
- Cabecera ("hero") con degradado de marca, logo, tipo de informe, título y metadatos.
- **Índice lateral fijo** con resaltado de la sección visible (en móvil pasa arriba).
- Tarjetas KPI, tablas con cabecera marino y bandas, callouts, figuras con pie numerado.
- Responsive (móvil/tablet/escritorio), semántico (`h2/h3`, `table`, `figure`), con `lang` correcto.
- Sin librerías externas ni fuentes remotas (fuente Calibri/Segoe/Arial del sistema).

## Cuándo usarlo
Ver [[Guia_de_eleccion_de_formato]]. Pensado para lectura en pantalla y para compartir resúmenes con clientes. No sustituye al DOCX/PDF cuando el documento es para registro o firma.

## Pendiente
Visores interactivos (comparador antes/después de fotomontajes, calendario de sombras) y gráficos con datos. Ver [[Ampliar_el_sistema]].
