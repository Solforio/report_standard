---
tags: [flujo, preguntas]
---
# Preguntas iniciales (Claude debe hacerlas antes de generar nada)

Se hacen con selección múltiple. Si el usuario ya ha dado la respuesta en su mensaje, no se repite la pregunta.

## 1. Idioma del informe *(una opción)*
- Español · Català · English
- Si pide varios idiomas → un archivo por idioma, mismo contenido traducido ([[Glosario_trilingue]]).

## 2. Tipo de informe *(una opción)*
Posicionamiento y viabilidad preliminar · Análisis energético y económico · Recurso eólico y producción · Impacto acústico · Sombras parpadeantes · Estudio visual · Accesos y transporte · Respuesta a requerimiento · Alternativas y modificaciones · Terrenos y propietarios · Normativa y urbanismo ([[00_Mapa_de_tipos]]).
*Sugerencia automática del formato principal según el tipo.*

## 3. Formatos *(selección múltiple)*
DOCX editable · PPTX editable · PDF · HTML. Proponer por defecto el principal del tipo + PDF ([[Guia_de_eleccion_de_formato]]). Explicar en una línea cuándo tiene sentido HTML.

## 4. Proyecto y cliente
Cliente, nombre del proyecto, emplazamiento (municipio/provincia), código de proyecto (p. ej. `KRON002`), versión (V01 por defecto), autores y validador, logo del cliente (si existe).

## 5. Datos y fuentes
¿Qué archivos o datos de partida hay? (cálculos, mapas, tablas, fotos). **Si no hay datos, no se inventan**: se crean secciones con campos pendientes marcados `[PENDIENTE]` o se genera un ejemplo marcado como tal (`example: true`).

## 6. Opciones adicionales *(solo si procede)*
Sello "Cálculos con WindPRO · EMD" · marca de borrador · destinatario (para cartas) · plantilla de portada con fotografía.

## Después de las respuestas
1. Resumir lo entendido en 3 líneas y pedir confirmación solo si hay ambigüedad.
2. Leer la ficha del tipo y el glosario del idioma.
3. Redactar el YAML ([[Esquema_YAML]]), generar, **revisar el resultado visualmente** y pasar [[Checklist_QA]].
4. Entregar archivos + 3–5 líneas con qué se ha generado, qué faltaba (pendientes) y supuestos hechos.
