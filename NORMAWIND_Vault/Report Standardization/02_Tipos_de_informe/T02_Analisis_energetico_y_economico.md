---
tags: [tipo, economico, energia]
doc_type: energetico_economico
formato_principal: pptx
estilo: deck
---
# T02 · Análisis energético y económico

**Propósito.** Cuantificar producción, uso de la energía (autoconsumo/excedentes) y rentabilidad de un proyecto eólico ya definido. Existe en dos formas:
- **Deck** (formato principal): módulo de análisis para cliente, normalmente integrado en [[T01_Posicionamiento_y_viabilidad_preliminar]] o como actualización.
- **Anexo de proyecto** (DOCX): *Estudio de viabilidad económico-financiera* del proyecto administrativo (`An07_Estudi viabilitat`, muestras Llers y Pujades).

## Estructura del anexo DOCX (muestra Llers/Pujades)
1. Objeto (turbina, potencia, municipio).
2. Contenido del estudio: viabilidad **económica** (ingresos y gastos) y **financiera** (cobros y pagos).
3. Resultados: datos fundamentales (inversión, potencia, coste de ejecución, ICIO, inversión/MW), financiación, horizonte (30 años), tasa de descuento, inflación.
4. Hipótesis: ingresos (precio de futuros OMIP y coeficiente de apuntamiento), impuestos y peajes, gastos de explotación (€/MW·año).
5. Parámetros de rentabilidad: **TIR, VAN, payback**; gráfico de flujo de caja acumulado.
6. Análisis de sensibilidad **±10 %** de: coste de inversión, coste de operación, precio de venta, producción.
7. Conclusión.

## Estructura del deck (ver T01 §9–10 y propuesta)
`input_data` → `turbine_description` → `wind_resource` → `energy_analysis` → `economic_analysis` → `sensitivity` → `conclusions`.

## Indicadores y definiciones (usar siempre las mismas)
| Indicador | Definición |
|---|---|
| **DevEx** | Gastos de desarrollo (estudios, tramitación, diseño) |
| **CapEx** | Inversión de construcción (turbina, obra civil, infraestructura eléctrica, ICIO…) |
| **OpEx** | Operación y mantenimiento anual (€/año o €/MW·año) |
| **LCOE** | Coste nivelado de la energía (€/MWh): ciclo de vida completo |
| **VAN / NPV** | Valor actual neto a la tasa de descuento indicada |
| **TIR / IRR** | Tasa interna de rentabilidad |
| **Payback** | Años hasta recuperar la inversión (DevEx + CapEx) |
| **PPA autoconsumo** | Precio de compra de la energía autoconsumida (€/MWh) |
| **Cobertura** | % de la demanda cubierta por la nueva generación |

## Hipótesis que siempre hay que declarar
Horizonte (histórico: 30 años), tasa de descuento (VAN 3,50 % en Llers), inflación (1 %), precio y su fuente **con fecha de consulta** (p. ej. futuros MIBEL SPEL de OMIP a abr-2026), impuestos (7 % sobre ingresos), peajes (0,5 €/MWh), ICIO (4 %), financiación (100 % fondos propios), pérdidas y disponibilidad.
> [!warning] Los valores anteriores son los del caso Llers (2026). **No son valores por defecto**: actualizar siempre con datos vigentes del proyecto.

## Elementos visuales
Tabla de costes por conceptos; tabla de resultados por escenario (promedio/máx/mín); flujo de caja acumulado (barras); *tornado* o líneas de sensibilidad; gráficos mensual y diario de generación vs demanda; tarta de cobertura (FV existente / eólica nueva / red).

## Mejoras respecto al histórico
- Hipótesis visibles en una tabla única "Hipótesis del análisis".
- Escenarios etiquetados igual en energía y economía.
- Notas al pie estandarizadas (definición de LCOE, 1 % de incremento anual…).
- Colores de marca en lugar de verde/amarillo/rosa de Excel pegado.

Muestras: `INFORMES/03_Viabilidad_economica/`, `INFORMES/04_Viabilidad_preliminar/KRONOSPAN_Salas/`. Ver [[Inventario_y_analisis]].
