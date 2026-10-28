---
tags: [formatos, pptx]
actualizado: 2026-10-28
---
# PPTX (presentación editable)

Generado con `render_pptx.py` (python-pptx). Todo son objetos nativos (formas, cuadros de texto, tablas, imágenes): editable sin pérdida. **Layout v2 (28/10/2026)**: calcado del histórico `20260310_KRON002 Viability Salas (VESTAS).pptx` (ver [[Inventario_y_analisis]]), por petición del equipo.

## Referencia histórica y resultado
| Histórico KRON002 (portada) | Facsímil generado |
|---|---|
| ![[referencia_KRON002_slide01.png]] | ![[pptx_portada.png]] |

## Especificación
- **16:9** (33,87 × 19,05 cm), fondo **blanco**, igual que las presentaciones históricas.
- Margen lateral **1,7 cm**; zona de contenido 3,4–17,5 cm; pie discreto a 18,2 cm: código · título corto a la izquierda; a la derecha nº de diapositiva y **logo NORMAWIND horizontal pequeño** (altura 0,6 cm, `normawind-horizontal-positive.png`).
- **Título = banda gris `#F2F2F2`** a todo el ancho (1,7 cm, y = 1,1 cm, alto 1,2 cm) con texto **en versalitas** (*small caps*) negro 20 pt. Si hay sección y subsección: «Sección – Subsección».
- **Portada y contraportada comparten retícula** (foto de 11,9 cm a la derecha con el **logo NORMAWIND horizontal girado 90° en la franja del borde derecho**, donde el histórico tenía una barra taupe) — ver abajo.
- **Separador de sección** (secciones con ≥ 2 subsecciones): banda gris a media altura con «n · Título».
- **Fuente: Abadi Extra Light** (la del histórico KRON002; solo PPTX, constante `FONT_PPTX` en `nwcommon.py`). Si el equipo no la tiene instalada, PowerPoint la sustituye; los PDF de decks deben exportarse en un equipo con la fuente.
- Cuerpo: texto 16–18 pt (14–16 pt con visual al lado), viñetas «•» con negrita inicial, subtítulos en negrita negra, espaciado generoso.
- Tablas: cabecera marino con texto blanco, filas sin cebra con línea fina inferior, números centrados, fila destacada / total en azul pálido. Menos de 4 columnas: no se estiran a todo el ancho; más de 9 filas se reparten en varias diapositivas.
- Callouts: recuadro de borde fino con texto en **cursiva** (como las notas a pie del histórico); gris = información, color = aviso/ok/crítico.
- Layouts automáticos: texto + figura (2 columnas); tabla pequeña + figura; dos figuras; KPI arriba + texto; callout bajo el texto.

## Portada y contraportada (idénticas en retícula)
![[pptx_portada.png]]
![[pptx_contraportada.png]]

**Portada** (coordenadas en cm, del histórico):
- Foto B/N a la derecha: `x 19,8 · y 0 · 11,9 × 19,05` — por defecto `assets/photos/cover_turbine_bw.jpg`; sustituible con `meta.cover_image` (se recorta al panel).
- **Logo NORMAWIND horizontal girado 90°** (legible de arriba abajo) en la franja derecha del borde, centro `x 32,8 · y 15,0`, largo 6,84 cm × alto 1,15 cm (en lugar de la barra taupe del histórico). Sin targeta blanca.
- Bloque de título `x 2,4 · y 2,2 · ancho 17`: tipo de informe (36 pt negrita marino) · título (22 pt) · subtítulo · proyecto – emplazamiento · fecha; todo en MAYÚSCULAS salvo la fecha.
- «CLIENTE:» (9 pt) en `x 2,7 · y 14,1`; **logo del cliente** `x 4,7 · y 13,0 · 5,2 × 2,9`; razón social en 7 pt debajo.
- **Logo NORMAWIND vertical** `x 7,8 · y 16,9 · ancho 2,7`.
- Etiqueta roja «EJEMPLO – DATOS FICTICIOS» arriba a la izquierda si `example: true`.

**Contraportada**:
- Foto B/N `assets/photos/closing_team_bw.png` en la misma posición que la de portada, con el mismo logo girado en el borde derecho (centro `x 32,9 · y 15,3`).
- Logo NORMAWIND vertical con lema, `x 5,5 · y 5,2 · ancho 7,8`.
- Dirección (2 líneas) y teléfono/web en dos columnas, 12 pt gris, `y 10,4`.
- Sello WindPRO · EMD abajo a la izquierda si `powered_by_emd: true`.

## Páginas de contenido
| Texto + tabla | Gráfico + tabla | KPI + callout |
|---|---|---|
| ![[pptx_contenido_tabla_texto.png]] | ![[pptx_grafico_tabla.png]] | ![[pptx_kpis_callout.png]] |

| Texto + figura | Comparativa | Gráfico circular |
|---|---|---|
| ![[pptx_figura_texto.png]] | ![[pptx_tabla_comparativa.png]] | ![[pptx_grafico_tarta.png]] |

Control de revisiones (tablas con cabecera gris y bordes finos, como el histórico):

![[pptx_control_revisiones.png]]

## Reglas de diseño
- **Una idea por diapositiva.** Títulos que enuncian el mensaje cuando sea posible.
- Máx. 6 viñetas por diapositiva.
- Gráficos con paleta de marca ([[Identidad_visual]]); sin 3D; etiquetas directas.
- Imágenes: mínimo 150 ppp; mapas con leyenda, escala y norte. En el histórico las láminas de mapa ocupan casi toda la diapositiva: dar a la figura ancho completo.
- Notas del orador: usar el campo de notas, no texto oculto.

## Diferencias aún abiertas respecto al histórico
- Tablas del histórico con bandas de color (verde/azul/amarillo según bloque de coste): aquí solo marino + azul pálido.
- Láminas de mapa a pantalla completa y gráficos nativos de Excel: ver [[Ampliar_el_sistema]].

## Limitaciones actuales
- Sin animaciones ni transiciones.
- Los gráficos se insertan como imagen (no gráficos nativos editables de PowerPoint).
- Las fotografías de portada/contraportada proceden del histórico KRON002 y se usan **para todos los informes** (decisión del equipo, 28/10/2026).
