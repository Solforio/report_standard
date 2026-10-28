---
tags: [tipo, recurso-eolico, aep]
doc_type: recurso_eolico
formato_principal: pdf
estilo: document
---
# T03 · Recurso eólico y producción (Site assessment / Energy yield)

**Propósito.** Estimar la producción anual neta de una o varias turbinas en un emplazamiento con incertidumbre (P50/P75/P90/P95), a partir de mediciones y series de largo plazo. Es un documento **técnico de cálculo**, normalmente en inglés para clientes internacionales (muestra Amazon MAD07, junio 2025).

## Estructura (muestra `03-018-25 Site Assessment Amazon MAD07`)
| Sección | Contenido |
|---|---|
| Portada + historial de revisiones + autor/aprobador + nombre/versión/referencia | Marcos estándar ([[Estructura_comun]]) |
| **Resumen ejecutivo** (`executive_summary`) | Turbina (modelo, altura de buje, rotor, clase IEC con Vref, Vave, TI15, α), layout (coordenadas ETRS89), **AEP neta**, tabla de probabilidades de excedencia |
| Alcance (`objective`) | Tareas: evaluación energética, pérdidas e incertidumbre, *site assessment* del layout; modelos y versiones (WAsP, WAsP Engineering, WindPRO) |
| Datos de entrada (`input_data`) | Posición, topografía/rugosidad, mediciones (LIDAR/mástil, periodo, filtrado, recuperación de datos), referencia de largo plazo |
| Recurso eólico (`wind_resource`) | Velocidad media, rosa de vientos, distribución de Weibull, turbulencia, cizalladura |
| Ajuste a largo plazo (`long_term_adjustment`) | Método (p. ej. *Scaling Local*), dataset (EMD-WRF ERA5, 20 años), coeficiente de correlación |
| Viento extremo y turbulencia | Vm50 por método de tormentas independientes (MIS), cumplimiento de clase IEC |
| Producción (`energy_analysis`) | Bruta, estelas (modelo N.O. Jensen), turbulencia efectiva (Frandsen 1999) |
| Pérdidas e incertidumbre (`losses_uncertainty`) | Tabla de pérdidas (disponibilidad, eléctricas, ambientales…), incertidumbres independientes y normales, vida útil 20 años |
| Resultados (`results`) | AEP P50/P75/P90/P95 a 1, 10 y 20 años; horas equivalentes |
| Conclusiones | AEP recomendada, riesgos |

## Datos y formatos
- Coordenadas **ETRS89 huso 30/31** (indicar siempre el huso).
- Tablas con unidades en cabecera; GWh/año con 3 decimales; horas equivalentes enteras.
- Cada tabla con título *"Tabla n. …"* y fuente del dato.

## Mejoras respecto al histórico
- Cabecera en todas las páginas con logo, título y fecha (la muestra ya lo hace; se mantiene).
- Resumen de **una página** con los resultados clave antes de la metodología.
- Referencias de modelos y versiones en tabla única.
- Mismo glosario EN/ES/CA ([[Glosario_trilingue]]) si se pide traducción.

> [!note] Las muestras `05_` y `06_` contienen el mismo PDF (informe de recurso y *site assessment* a la vez). En el sistema, ambos son este tipo.

Muestra: `INFORMES/05_Recurso_eolico_y_produccion/`. Ver [[Inventario_y_analisis]]. Relacionado: [[T05_Sombras_parpadeantes]] (reutiliza el recurso en el emplazamiento).
