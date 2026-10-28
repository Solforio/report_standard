---
name: normawind-reports
description: Genera informes estandarizados de NORMAWIND S.L. (viabilidad y posicionamiento de aerogenerador, análisis energético-económico, recurso eólico, impacto acústico, sombras parpadeantes, estudio visual, accesos y transporte, respuestas a requerimientos, alternativas, terrenos, normativa) en DOCX, PPTX, PDF y HTML, en español, catalán o inglés, con la marca corporativa. Úsala siempre que se pida crear, rehacer, traducir o estandarizar un informe, memoria, anexo, presentación de viabilidad o carta a una administración para NORMAWIND.
---

# Skill: informes NORMAWIND

Convierte un contenido técnico en informes con **estructura, estilo e idioma estandarizados**. El conocimiento está en el vault de Obsidian `NORMAWIND_Vault/Report Standardization/` (abrir esa carpeta como vault; está en la raíz del proyecto, dos niveles por encima de `.claude/`; las imágenes están en `Adjuntos/`); el generador está en `scripts/`.

## Si falta el vault en local
El repositorio público `https://github.com/Solforio/report_standard` contiene la skill y el vault. Si `NORMAWIND_Vault/Report Standardization/` no existe en el proyecto, clónalo (`git clone --depth 1 https://github.com/Solforio/report_standard <carpeta-temporal>`) y lee las notas desde ahí; no inventes reglas ni glosario. Las muestras históricas (`INFORMES/`, `05_Muestras_historicas/`) no están en el repositorio por contener datos de clientes.

## Flujo obligatorio

### 1. Preguntar (si el usuario no lo ha dicho ya)
Lee `NORMAWIND_Vault/Report Standardization/06_Flujo_de_trabajo/Preguntas_iniciales.md`. Usa la herramienta de preguntas con **selección múltiple**:
1. **Idioma**: Español / Català / English (un archivo por idioma si pide varios).
2. **Tipo de informe** (11 tipos; `build_report.py --list-types`).
3. **Formatos** (múltiple): DOCX editable · PPTX editable · PDF · HTML. Propón por defecto el principal del tipo + PDF; menciona HTML solo cuando tiene sentido (`04_Formatos/Guia_de_eleccion_de_formato.md`).
4. **Proyecto**: cliente, proyecto, emplazamiento, código, versión, autores/validador, logo del cliente.
5. **Datos de partida**: qué archivos/cálculos hay. **Nunca inventes cifras.** Sin datos → marca `[PENDIENTE]` o genera un ejemplo con `meta.example: true` y dilo claramente.

### 2. Leer el conocimiento (solo lo necesario)
- Ficha del tipo: `NORMAWIND_Vault/Report Standardization/02_Tipos_de_informe/T##_*.md` (estructura, datos, criterios, mejoras).
- `01_Marca/Estructura_comun.md` y `Estilo_de_redaccion.md`.
- `03_Idiomas/Glosario_trilingue.md` y `Formulas_y_formatos_por_idioma.md` del idioma elegido.
- Si hace falta ver cómo eran los históricos: `05_Muestras_historicas/` y `INFORMES/` (solo estructura; **no copies datos** de otros proyectos).

### 3. Redactar el contenido en YAML
Esquema en `NORMAWIND_Vault/Report Standardization/06_Flujo_de_trabajo/Esquema_YAML.md`; ejemplos funcionales en `examples/` (`demo_viabilidad_es.yaml`, `demo_acustico_ca.yaml`, `demo_respuesta_en.yaml`).
- Escribe **todo en el idioma elegido** (títulos de sección estándar salen solos con `id:`), con el formato numérico del idioma.
- Sigue las secciones estándar del tipo (`data/report_types.yaml`; `*` = obligatorias). Resumen ejecutivo primero en viabilidad.
- Figuras: rutas relativas al YAML. Gráficos: bloque `chart:` (paleta de marca) en lugar de imágenes externas cuando sean datos simples.
- Guarda el YAML junto a la salida (p. ej. `<carpeta del proyecto>/informes/AAAAMMDD_CODIGO.yaml`) para poder regenerar.

### 4. Generar
```bash
python -I .claude/skills/normawind-reports/scripts/build_report.py CONTENIDO.yaml --formats docx,pdf,html --out SALIDA
```
- `--formats`: lista de `docx,pptx,pdf,html`. El PDF se exporta desde el DOCX (documentos/cartas) o desde el PPTX (presentaciones) con Word/PowerPoint instalados.
- Nombre automático: `AAAAMMDD_CÓDIGO_Titulo_IDIOMA.ext`.
- Si falla la validación, corrige el YAML (ids de sección, imágenes, secciones obligatorias).
- Dependencias: ver `requirements.txt` (`pip install -r ...`).

### 5. Revisar visualmente (no te saltes este paso)
```bash
python -I .claude/skills/normawind-reports/scripts/preview.py SALIDA/archivo.pdf --pages 1-12 --out SALIDA/_preview.png
```
Abre la imagen y comprueba: portada, índice con páginas, tablas no partidas, figuras legibles, sin desbordes, sin páginas casi vacías, etiquetas en el idioma correcto. Para HTML, ábrelo en el navegador. Corrige el YAML y regenera. Después pasa `06_Flujo_de_trabajo/Checklist_QA.md`.
Borra los archivos de previsualización antes de entregar.

### 6. Entregar
Informa en pocas líneas: archivos generados (rutas), qué datos **faltaban** o quedan `[PENDIENTE]`, y los **supuestos** hechos. Si es un ejemplo, recuérdalo.

## PPTX: layout v2 (calcado del histórico KRON002)
Banda gris con título en versalitas, fondo blanco, **portada y contraportada con la misma retícula** (foto B/N a la derecha en `assets/photos/`, barra taupe, logo NORMAWIND vertical, logo del cliente, contacto). Foto propia: `meta.cover_image`. Detalle y capturas en `NORMAWIND_Vault/Report Standardization/04_Formatos/PPTX.md`. Si cambias el renderer, regenera los ejemplos con `bash .claude/skills/normawind-reports/examples/build_facsimiles.sh`. Si un PDF/PPTX falla por estar abierto en Office, ciérralo y repite (no mates procesos de Office).

## Reglas
- Un idioma por documento. Terminología del glosario; términos catalanes marcados (¿) → avisar de que requieren validación.
- Datos personales (propietarios, teléfonos) solo en informes internos; marcar `confidential: true`.
- No cites normas sin comprobar vigencia; indica fecha de consulta.
- Si el usuario pide un tipo o sección que no existe, sigue `06_Flujo_de_trabajo/Ampliar_el_sistema.md` y propón el cambio antes de improvisar.
- El editable (DOCX/PPTX) es la entrega "viva"; si hay que cambiar algo grande, edita el YAML y regenera para mantener los formatos sincronizados.

## Archivos
```
scripts/  nwcommon.py (marca, i18n, carga) · nwcharts.py · render_docx.py · render_pptx.py · render_html.py
          build_report.py (CLI) · office_export.ps1 (Word/PowerPoint → PDF) · preview.py
data/     strings.yaml (etiquetas/títulos EN·ES·CA) · report_types.yaml (tipos y secciones)
assets/logos/  NORMAWIND y EMD (PNG)      assets/photos/  fotos B/N portada y contraportada
examples/  YAML de demostración, facsimiles/ y build_facsimiles.sh
```
