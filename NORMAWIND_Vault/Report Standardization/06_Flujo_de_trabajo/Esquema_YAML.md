---
tags: [flujo, yaml, tecnico]
---
# Esquema del contenido (YAML)

El informe se escribe **una vez** en un archivo `.yaml`; la skill genera DOCX, PPTX, PDF y HTML desde él. Ejemplos funcionales en `examples/`. Plantilla en blanco: [[contenido_base]].

## `meta` (datos del documento)
| Campo | Obligatorio | Descripción |
|---|---|---|
| `doc_type` | sí | id del tipo ([[00_Mapa_de_tipos]]) |
| `lang` | sí | `es` · `ca` · `en` |
| `title` | sí | Título completo (portada) |
| `short_title` | recomendado | Título corto para cabecera/pie y nombre de archivo |
| `subtitle` | no | Subtítulo (p. ej. cliente + planta) |
| `client`, `project`, `location` | recomendado | Portada y ficha |
| `code` | recomendado | Código de proyecto (KRON002…) |
| `date` | sí | `AAAA-MM-DD` |
| `version` | no (V01) | `V01`, `V02`… |
| `authors` | recomendado | Lista de autores |
| `validated_by` | recomendado | Validador |
| `revisions` | no | Lista `{version, date, changes}`; por defecto una fila "Primera versión" |
| `client_logo` | no | Ruta a imagen (relativa al YAML) |
| `cover_image` | no | Foto de portada del PPTX (relativa al YAML); por defecto la foto B/N del aerogenerador. Se recorta al panel 11,9 × 19,05 cm |
| `powered_by_emd` | no | `true` → sello WindPRO/EMD en cierre de PPTX |
| `example` / `draft` | no | Marca roja de ejemplo / borrador |
| `confidential` | no (true) | Aviso de confidencialidad en el pie |
| `doc_name` | no | Nombre del documento en la ficha de control |
| **Cartas**: `recipient` (lista), `subject`, `reference_lines` (lista de `[etiqueta, valor]`), `place_date` | | Solo para `respuesta_requerimiento` |

## `sections`
Lista ordenada. Cada elemento:
```yaml
- id: site_analysis          # id estándar (traducción automática del título) – ver data/strings.yaml
  title: "..."               # opcional: sustituye al título estándar
  blocks: [ ... ]            # contenido directo de la sección
  subsections:               # opcional
    - title: "Restricciones técnicas"
      blocks: [ ... ]
```
Un id nuevo necesita sus tres traducciones en `strings.yaml`. Una sección sin `id` necesita `title`.

## Bloques (`blocks`)
| Bloque | Sintaxis |
|---|---|
| Párrafo | `- p: "Texto con **negrita** y *cursiva*."` |
| Viñetas | `- bullets: ["a", "b"]` |
| Lista numerada | `- numbered: ["a", "b"]` (cada lista reinicia en 1) |
| Subtítulo | `- subheading: "Texto"` |
| Tabla | `- table: {caption, header: [..], rows: [[..]], widths: [..], source, total_row: true}` |
| Clave–valor | `- keyvalue: {caption, rows: [[clave, valor], ...]}` |
| Figura | `- figure: {path, caption, source, width_cm}` |
| Gráfico | `- chart: {kind: bar\|stacked\|line\|pie, labels, series: [{name, values}], ylabel, xlabel, title, caption, width_cm}` → se genera con la paleta de marca |
| KPI | `- kpis: [{label, value, unit}]` (3–5 tarjetas) |
| Llamada | `- callout: {kind: info\|warn\|ok\|bad, title, text}` |
| Salto de página | `- pagebreak: true` (solo DOCX) |

Reglas: cifras como **texto ya formateado** según el idioma (`"13.070"`, `"13,7"`); rutas de imagen relativas al YAML; PNG/JPG, ≥ 150 ppp.

## Generar
```bash
python -I .claude/skills/normawind-reports/scripts/build_report.py contenido.yaml --formats docx,pdf --out salida
python -I .claude/skills/normawind-reports/scripts/build_report.py --list-types
```
Valida: id de tipo y de sección, imágenes existentes, secciones obligatorias del tipo (avisa si faltan).
