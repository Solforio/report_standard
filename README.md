# NORMAWIND · Estandarización de informes

| Carpeta | Contenido |
|---|---|
| `INFORMES/` | Biblioteca de informes históricos organizados por tipo (136 archivos). Inspiración, no plantillas de datos. Índice de origen en `00_Indice_origen.csv`. |
| `LOGO/` | Logotipos oficiales NORMAWIND y EMD. |
| `NORMAWIND_Vault/Report Standardization/` | **Base de conocimiento (Obsidian)**, con capturas de ejemplo en `Adjuntos/`; hay una copia espejo en Notion: marca, estructura común, fichas de los 11 tipos de informe, glosario ES·EN·CA, formatos, auditoría de los históricos y flujo de trabajo. Abrir esa carpeta como *vault* en Obsidian; empezar por `00_Inicio.md`. |
| `FACSIMILES/` | 11 informes de ejemplo (uno por tipo) con datos ficticios, en DOCX, PPTX y PDF. Fuentes YAML en `.claude/skills/normawind-reports/examples/`. |
| `.claude/skills/normawind-reports/` | **Skill de Claude** y generador (DOCX · PPTX · PDF · HTML). `SKILL.md` describe el flujo; `examples/` contiene ejemplos con datos ficticios y sus salidas en `examples/salida_demo/`. |

## Uso rápido
Pedir a Claude, desde esta carpeta: *"Hazme el informe de sombras parpadeantes de X"*. Claude preguntará idioma, tipo, formatos y proyecto, leerá el vault, redactará el contenido y generará los archivos.

Instalar dependencias una vez: `pip install -r .claude/skills/normawind-reports/requirements.txt` (Python 3.10+; Word y PowerPoint para exportar a PDF).


## Repositorio en GitHub
Este contenido está en https://github.com/Solforio/report_standard (público). Para usarlo: `git clone`, abrir la carpeta con Claude Code, instalar dependencias (`pip install -r .claude/skills/normawind-reports/requirements.txt`) y tener instalada la fuente Abadi Extra Light para los PPTX. **No incluidos** (datos de clientes o material pesado): `INFORMES/`, `LOGO/`, `FACSIMILES/` (se regeneran con `examples/build_facsimiles.sh`) y las notas de muestras históricas del vault.
