---
tags: [marca, estilo]
---
# Identidad visual

Extraída de los logotipos oficiales (carpeta `LOGO/`) y de los informes históricos. Los valores viven en `scripts/nwcommon.py` de la skill; si cambian aquí, cambiarlos allí.

## Vista rápida
![[paleta_marca.png]]

| Logo vertical | Logo horizontal | EMD |
|---|---|---|
| ![[logo_normawind-positive.png\|160]] | ![[logo_normawind-horizontal-positive.png\|260]] | ![[logo_emd-black.png\|140]] |

## Paleta
| Token | HEX | Uso |
|---|---|---|
| **Azul marino** `NAVY` | `#103870` | Títulos, cabeceras de tabla, bloque de portada, texto de marca |
| **Azul** `BLUE` | `#1868D0` | Acentos, numeración, KPI, líneas, hipervínculos |
| **Azul cielo** `SKY` | `#5FA8F0` | Etiquetas sobre fondo oscuro, series de gráfico |
| **Taupe** `TAUPE` | `#A89080` | Etiquetas secundarias (lema "Green energy consulting"), pie de confidencialidad |
| **Beige** `BEIGE` | `#E8DCCB` | Subtítulos sobre fondo oscuro, filete de portada |
| **Tinta** `INK` | `#1F2933` | Texto de cuerpo |
| **Gris** `GREY` | `#5B6470` | Pies de figura, fuentes, cabecera/pie |
| **Azul pálido** `PALEBLUE` | `#DCE8F8` | Celdas de etiqueta, fila de total |
| **Gris claro** `LIGHT` | `#F3F5F8` | Bandas alternas de tabla, tarjetas KPI |
| Estados | OK `#2E8B57` · Aviso `#D98E04` · Crítico `#C0392B` | Solo para llamadas (callouts) y semáforos |

**Series de gráficos (orden):** azul → marino → taupe → cielo → gris azulado → beige oscuro. Máximo 6 series; más de 4 → replantear el gráfico. No usar rojo/verde como únicas diferencias (daltonismo): añadir etiqueta o patrón.

## Tipografía
- **PPTX: Abadi Extra Light** (como el histórico KRON002). **DOCX/HTML/PDF de documento: Calibri**.
- Calibri en los demás formatos (disponible en Office, Windows y Mac; es la fuente dominante en los PDF históricos). Cuerpo 10,5 pt (DOCX) · 16–20 pt (PPTX).
- Títulos en negrita, color marino; H3 en azul. **Nada de MAYÚSCULAS en títulos** (el histórico mezclaba mayúsculas, minúsculas y "AnàlisI acústicA"). Excepciones en **PPTX**: portada en mayúsculas y títulos de diapositiva en **versalitas** sobre banda gris, como el histórico KRON002.
- El logotipo usa una tipografía extendida propia: **no se reproduce con texto**, se usa siempre el archivo del logo.

## Logotipos (`LOGO/NORMAWIND`, copiados en `assets/logos/` de la skill)
| Archivo | Cuándo |
|---|---|
| `normawind-horizontal-positive.png` | Fondo claro: cabecera de DOCX, **logo pequeño en el pie de cada diapositiva PPTX**, logo girado 90° en el borde derecho de portada/contraportada PPTX, HTML. Es la mejor opción de `LOGO/NORMAWIND` (transparente, 874 px, color); las variantes `_petit`/`_tallat`/`_comprimida` tienen menos resolución |
| `normawind-horizontal-negative.png` | Fondo oscuro/azul: portada y cierre de PPTX, hero HTML |
| `normawind-positive.png` / `-negative.png` | Versión vertical (isotipo + texto + lema): **portada y contraportada del PPTX**, espacios cuadrados |
| `normawind-negative-background-horizontal.png` | Imagen de fondo con degradado azul–beige (portadas especiales, redes) |

Reglas: respetar proporciones; zona de respeto ≥ la altura de la "M" del isotipo; altura mínima 0,7 cm en pie de página; no recolorear ni añadir sombras.

### Logotipo EMD (`LOGO/EMD`)
Dos versiones (negro/blanco). **Nota técnica:** los archivos `.png` originales son en realidad SVG renombrados; la skill los convierte a PNG real.
Uso previsto: sello **"Cálculos con WindPRO · EMD"** en estudios que usan WindPRO (recurso eólico, acústico, sombras). Se activa con `powered_by_emd: true`. Confirmar con el equipo las condiciones de uso de marca de EMD antes de usarlo en documentos para terceros.

### Logotipo del cliente
`client_logo` en el YAML; se coloca en portada, sobre fondo blanco, altura ≈ 1,6 cm. Pedir siempre el archivo al cliente; no copiarlo de otros informes sin permiso.

## Marcado de documentos de ejemplo/borrador
- `example: true` → etiqueta roja "EJEMPLO – DATOS FICTICIOS" en portada, cabecera y pie.
- `draft: true` → etiqueta "BORRADOR". Quitar antes de entregar.
