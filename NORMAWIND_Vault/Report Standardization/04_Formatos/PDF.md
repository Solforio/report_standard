---
tags: [formatos, pdf]
---
# PDF

**Nunca se compone aparte**: se exporta desde el DOCX (informes tipo documento/carta) o desde el PPTX (informes tipo presentación), usando Word/PowerPoint instalados (script `office_export.ps1`). Así el PDF coincide exactamente con el editable.

- DOCX → PDF: se actualizan índice y campos antes de exportar (paginación correcta en el índice).
- PPTX → PDF: una diapositiva por página, 16:9.
- Metadatos: título y autor del documento.
- Entrega a cliente/administración: **PDF**; archivo interno: DOCX/PPTX + PDF.
- Si Word/PowerPoint no están instalados, la skill avisa y entrega solo el editable (opción `--no-office`).

Controles previos a entregar: ver [[Checklist_QA]] (índice actualizado, figuras legibles, sin marca de borrador/ejemplo, número de páginas correcto).
