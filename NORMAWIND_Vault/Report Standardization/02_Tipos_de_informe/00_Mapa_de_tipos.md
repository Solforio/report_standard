---
tags: [tipos, mapa]
---
# Mapa de tipos de informe

Cada tipo tiene un `id` (el que se escribe en `meta.doc_type` del YAML), un formato principal recomendado y una ficha con estructura, datos necesarios y criterios. La lista de secciones estándar está también en `data/report_types.yaml` de la skill (las marcadas `*` son obligatorias).

| # | Tipo (`doc_type`) | Principal | Otros | Estilo | Muestras en `INFORMES` |
|---|---|---|---|---|---|
| T01 | [[T01_Posicionamiento_y_viabilidad_preliminar]] (`posicionamiento_viabilidad`) | PPTX | PDF, DOCX, HTML | deck | `04_Viabilidad_preliminar` (28) |
| T02 | [[T02_Analisis_energetico_y_economico]] (`energetico_economico`) | PPTX | PDF, DOCX, HTML | deck | `03_Viabilidad_economica`, secciones de T01 |
| T03 | [[T03_Recurso_eolico_y_produccion]] (`recurso_eolico`) | PDF | DOCX | documento | `05_`, `06_Site_assessment` |
| T04 | [[T04_Impacto_acustico]] (`impacto_acustico`) | DOCX | PDF | documento | `01_Impacto_acustico` |
| T05 | [[T05_Sombras_parpadeantes]] (`sombras_parpadeantes`) | DOCX | PDF, HTML | documento | `02_Sombras_parpadeantes` |
| T06 | [[T06_Estudio_visual]] (`estudio_visual`) | PDF | DOCX, HTML | documento | `07_Estudios_visuales` |
| T07 | [[T07_Accesos_y_transporte]] (`accesos_transporte`) | DOCX | PDF | documento | `08_Accesos_y_transporte` |
| T08 | [[T08_Respuesta_a_requerimiento]] (`respuesta_requerimiento`) | DOCX | PDF | carta | `09_Respuestas_a_requerimientos` |
| T09 | [[T09_Alternativas_y_modificaciones]] (`alternativas_modificaciones`) | DOCX | PDF, PPTX | documento | `10_Alternativas_y_modificaciones` |
| T10 | [[T10_Terrenos_y_propietarios]] (`terrenos_propietarios`) | DOCX | PDF | documento | `12_Terrenos_y_propietarios` |
| T11 | [[T11_Normativa_y_urbanismo]] (`normativa_urbanismo`) | DOCX | PDF, PPTX | documento | `13_Normativa_y_urbanismo` |

> [!note] No son tipos de informe (de momento)
> `11_Seguimiento_tramitacion` (historiales de trámite en Excel) y `14_Proyecto_completo_Llers` (proyecto administrativo completo) quedan como **referencia**. El seguimiento en Excel podría ser un 5.º formato (XLSX) en una fase posterior; el proyecto completo se compone de varios informes de estos tipos más anexos de ingeniería.

## Cómo elegir
- ¿Hay que **decidir o presentar** a un cliente (viabilidad, alternativas)? → presentación (PPTX) + PDF.
- ¿Es un documento **técnico a presentar a una administración** o a incluir como anexo de un proyecto? → DOCX editable + PDF.
- ¿Es un informe de **cálculo con resultados cerrados** que no debe modificarse (recurso eólico)? → PDF (con DOCX de origen).
- ¿Hay **mapas/gráficos interactivos o lectura en pantalla** (estudio visual, sombras)? → ofrecer HTML. Ver [[Guia_de_eleccion_de_formato]].
