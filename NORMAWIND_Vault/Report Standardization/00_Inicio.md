---
tags: [inicio, mapa]
actualizado: 2026-10-28
notion: espejo en Notion («Report Standardization»)
---
# NORMAWIND · Sistema de informes estandarizados

Base de conocimiento para generar informes con **la misma estructura, estilo y calidad** en cualquier idioma (EN · ES · CA) y formato (DOCX · PPTX · PDF · HTML). Está pensada para que la lea **Claude** (a través de la skill `normawind-reports`) y para que el equipo la consulte y la mejore desde Obsidian.

> [!info] Cómo se usa
> 1. Pides un informe a Claude ("hazme el estudio de sombras de X").
> 2. Claude te pregunta **idioma, tipo de informe, formatos, proyecto/cliente** ([[Preguntas_iniciales]]).
> 3. Lee la ficha del tipo ([[00_Mapa_de_tipos]]), la marca ([[Identidad_visual]]) y el glosario ([[Glosario_trilingue]]).
> 4. Redacta el contenido en un único archivo YAML ([[Esquema_YAML]]) y genera los formatos pedidos desde esa misma fuente.
> 5. Pasa la lista de comprobación ([[Checklist_QA]]) y te entrega los archivos.

## Mapa
- **Marca y estructura común**: [[Identidad_visual]] · [[Estructura_comun]] · [[Estilo_de_redaccion]]
- **Tipos de informe**: [[00_Mapa_de_tipos]]
- **Idiomas**: [[Glosario_trilingue]] · [[Formulas_y_formatos_por_idioma]]
- **Formatos**: [[Guia_de_eleccion_de_formato]] · [[DOCX]] · [[PPTX]] · [[PDF]] · [[HTML]]
- **Muestras históricas**: [[Inventario_y_analisis]] · [[Hallazgos_de_auditoria]]
- **Flujo de trabajo**: [[Preguntas_iniciales]] · [[Esquema_YAML]] · [[Checklist_QA]] · [[Ampliar_el_sistema]]

## Galería
| Portada PPTX | Contraportada PPTX | Contenido PPTX |
|---|---|---|
| ![[pptx_portada.png]] | ![[pptx_contraportada.png]] | ![[pptx_grafico_tabla.png]] |

| DOCX · portada | DOCX · cuerpo | Carta |
|---|---|---|
| ![[docx_T04_p1.png]] | ![[docx_T04_p3.png]] | ![[docx_T08_carta_p1.png]] |

## Dónde vive y cómo se mantiene
- Repositorio público: https://github.com/Solforio/report_standard (skill + este vault). Copia espejo en Notion.
- La skill usa **este vault en local primero**; si no existe, descarga el repositorio y lo usa como base.
- Cada cambio relevante se refleja a la vez en la skill, en este vault (con capturas en `Adjuntos/`) y en Notion; ver [[Ampliar_el_sistema]].

## Principios
1. **Una fuente, varios formatos.** El contenido se escribe una vez; los formatos son vistas del mismo texto, tablas y figuras.
2. **Evolución, no ruptura.** Se conserva la lógica de los informes históricos (portada → control de revisiones → índice → cuerpo numerado) y se corrigen sus inconsistencias ([[Hallazgos_de_auditoria]]).
3. **Un informe, un idioma.** Nada de mezclar idiomas en el mismo documento (el histórico lo hacía en varias presentaciones).
4. **Los datos no se inventan.** Toda cifra procede del proyecto, de un cálculo o de una fuente citada. Las muestras históricas son **modelos de estructura, no de datos**.
5. **Editable por defecto.** DOCX y PPTX con estilos reales; el PDF se genera siempre desde ellos.

## Estado
- Versión 1 del sistema: 11 tipos de informe, 4 formatos, 3 idiomas, marca extraída de los logotipos oficiales.
- Pendiente de validar por el equipo: terminología catalana específica de sombras/visual, paleta tipográfica final, plantilla de portada con fotografía. Ver [[Ampliar_el_sistema]].
