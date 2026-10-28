---
tags: [formatos]
---
# Guía de elección de formato

| Formato | Es lo mejor para | Evitar cuando |
|---|---|---|
| [[DOCX]] (editable) | Documentos técnicos que se presentan a administraciones, anexos de proyecto, textos largos que el equipo seguirá editando | Presentaciones de decisión a cliente |
| [[PPTX]] (editable) | Viabilidad y alternativas presentadas a clientes, reuniones, resúmenes visuales | Textos normativos largos |
| [[PDF]] | Entrega final, firmas, archivo; informes de cálculo cerrados. **Siempre se genera desde el DOCX/PPTX**, nunca se edita | Cuando el cliente pide versión editable |
| [[HTML]] | Lectura en pantalla, enlaces, gráficos/mapas interactivos, visores de puntos de vista, panel de resultados | Documentos formales para registro administrativo |

## ¿Cuándo tiene sentido HTML?
Sí: estudio visual (visor de PV), sombras (calendario interactivo), viabilidad como resumen web para el cliente, informes que se consultan en reunión. **No** para: respuestas a requerimientos, anexos de proyecto, informes que se imprimen/firman. El HTML es un único archivo autónomo (sin dependencias de red) que se puede enviar por correo o imprimir a PDF.

## Combinaciones recomendadas por tipo
| Tipo | Principal | Complementarios |
|---|---|---|
| T01 Viabilidad/posicionamiento | PPTX | PDF (entrega) · HTML (resumen web) · DOCX (si el cliente quiere memoria) |
| T02 Energético-económico | PPTX | PDF · DOCX (anexo de proyecto) |
| T03 Recurso eólico | PDF | DOCX (editable) |
| T04 Acústico · T05 Sombras | DOCX | PDF · HTML (sombras) |
| T06 Visual | PDF | HTML (visor) · DOCX |
| T07 Accesos · T09 Alternativas · T10 Terrenos · T11 Normativa | DOCX | PDF |
| T08 Respuesta a requerimiento | DOCX | PDF |

## Reglas transversales
- Todas las salidas parten del **mismo YAML**: cambia solo la presentación.
- Nombre: `AAAAMMDD_CÓDIGO_Titulo_IDIOMA.ext` ([[Estructura_comun]]).
- Si se pide más de un idioma, se genera **un archivo por idioma** (no bilingües).
- El PDF de un DOCX conserva índice y numeración (se actualizan los campos antes de exportar).
