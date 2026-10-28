---
tags: [tipo, administracion, carta]
doc_type: respuesta_requerimiento
formato_principal: docx
estilo: letter
---
# T08 · Respuesta a requerimiento / informe de organismo

**Propósito.** Contestar punto por punto a un informe, requerimiento de subsanación o informe de suficiencia de una administración u organismo (ADIF, Agricultura, Carreteras…). Es un documento **institucional**, formato carta, no un informe con portada. Muestras: *Resposta informe ADIF* (BCN4, 2024), *Resposta req AGR Salancs* (2026).

## Estructura (muestras)
1. **Membrete** NORMAWIND y **destinatario** (departamento, servicio territorial).
2. Fecha y lugar.
3. Bloque **ASUNTO / Expediente / Solicitante (CIF) / Potencia de la instalación (kW) / Nombre de la instalación** — se renderiza como tabla de referencia.
4. **Antecedentes** (`background`): qué se presentó y cuándo, qué informe se recibe.
5. **Resumen del requerimiento** (`request_summary`): lista numerada de puntos exigidos (copiar numeración del organismo).
6. **Respuesta** (`response`): una subsección por punto, con el mismo número/título que el requerimiento. Tablas, planos o fotografías si son necesarios; **referencias a anexos**.
7. **Conclusión** (opcional) y fórmula de cierre.
8. **Firma**: nombre, cargo, NORMAWIND S.L.

## Reglas específicas
- Misma **numeración y orden** que el requerimiento; el lector debe poder cotejar.
- Citar el artículo exacto de la norma cuando se justifica.
- Idioma = el del expediente (normalmente catalán o español).
- Sin cabecera en la primera página; sí en las siguientes. Sin índice. Sin marca "confidencial" salvo petición.
- Datos de expediente exactos (revisar números): un error en el nº de expediente invalida el escrito.

## Campos YAML de la carta
`meta.recipient` (lista de líneas), `meta.subject`, `meta.reference_lines` ([etiqueta, valor]…), `meta.place_date`.
Ejemplo: `examples/demo_respuesta_en.yaml`.

## Mejoras respecto al histórico
Las muestras usaban Bell MT/Times New Roman y márgenes de 3 cm sin identidad visual: ahora membrete de marca, tabla de referencia y tipografía única, manteniendo la sobriedad de una carta oficial.

Muestras: `INFORMES/09_Respuestas_a_requerimientos/`. Relacionado: [[T11_Normativa_y_urbanismo]].
