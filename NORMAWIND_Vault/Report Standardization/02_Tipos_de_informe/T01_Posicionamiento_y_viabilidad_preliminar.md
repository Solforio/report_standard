---
tags: [tipo, viabilidad, posicionamiento, pptx]
doc_type: posicionamiento_viabilidad
formato_principal: pptx
estilo: deck
---
# T01 · Posicionamiento de turbina y viabilidad preliminar

**Propósito.** Determinar si es viable implantar uno o varios aerogeneradores en un emplazamiento (normalmente para **autoconsumo industrial**), dónde colocarlos, cuánta energía producirán y qué rentabilidad preliminar tienen. Es el informe "de entrada" de un proyecto.

**Cuándo.** Fase de prospección/oportunidad, antes de medir viento y de iniciar la tramitación. Audiencia: cliente (dirección/energía) y equipo de desarrollo.

## Estructura estándar
Basada en las presentaciones de L'ENERGÈTICA (FGC, Puig de les Basses, Campredó…), ENDE001 Bon Preu y KRON002/Kronospan. Orden propuesto (id de sección entre paréntesis):

| # | Sección | Qué incluir | Diapositivas |
|---|---|---|---|
| 1 | Resumen ejecutivo (`executive_summary`) | **Al principio** (en el histórico iba al final o en medio). Ficha-resumen: turbina propuesta, producción neta, cobertura de demanda, LCOE/VAN/TIR/payback, conclusión en una frase | 1 |
| 2 | Objeto (`objective`) y alcance (`scope`) | Qué se evalúa y hasta qué radio (histórico: **5 km** alrededor del punto de consumo) | 1–2 |
| 3 | Marco normativo (`regulatory_framework`) | Solo lo que condiciona el proyecto (ver abajo). Una diapositiva por norma, máximo 4 | 2–4 |
| 4 | Metodología (`methodology`) | Mapa de recurso, cálculo de producción, balance energético horario, análisis económico | 1–2 |
| 5 | Descripción del emplazamiento (`site_description`) | Localización, ámbito de estudio, orografía, datos de la planta/consumo | 2–3 |
| 6 | Análisis de emplazamiento y restricciones (`site_analysis`) | Subsecciones: *urbanística*, *ambiental*, *técnica* (infraestructuras, viviendas, aeronáutica), *inundabilidad* | 4–8 |
| 7 | Recurso eólico (`wind_resource`) | Mapa a 100 m, rosa de energía, velocidad media, sector predominante | 1–2 |
| 8 | Propuesta técnica (`technical_proposal`) y alternativas (`alternatives`) | Mapa con posiciones; tabla comparativa de alternativas con semáforos; turbina (fabricante, modelo, potencia, rotor, altura de buje) | 2–4 |
| 9 | Análisis energético (`energy_analysis`) | Producción bruta/neta, horas equivalentes, perfil mensual y diario, balance generación–demanda, autoconsumo/excedentes | 2–4 |
| 10 | Análisis económico (`economic_analysis`) | DevEx, CapEx, OpEx, desmantelamiento; LCOE, VAN, TIR, payback, ahorro; flujo de caja; sensibilidades | 2–4 |
| 11 | Conclusiones (`conclusions`) y próximos pasos (`next_steps`) | Fortalezas/amenazas; acciones: validación con cliente, visita de campo, estudios ambientales, tramitación | 2 |
| 12 | Anexos (`annexes`) | Flujos de caja, recopilación fotográfica | n |

## Datos de entrada necesarios
Curva de consumo horaria (y FV existente si hay), coordenadas del punto de consumo, series de viento de largo plazo (mesoescala), curvas de potencia de la turbina candidata, costes unitarios (DevEx/CapEx/OpEx), precio de energía/PPA, cartografía de restricciones.

## Criterios y referencias habituales (de las muestras)
- **Distancia de seguridad** a carreteras, ferrocarriles y líneas AT: **1,5 × altura de punta de pala** (ej.: punta de pala 165 m → 247,5 m).
- **Servidumbres aeronáuticas**: pueden hacer inviable el emplazamiento (caso Illescas: zona de restricción de la base aérea de Getafe con punta de pala máx. 150 m).
- **Fauna**: criterios para compatibilizar renovables con *águila cuabarrada*, águila de Bonelli (zonas de exclusión).
- **Normativa**: Decret-llei 16/2019 (Cataluña), RD 244/2019 (autoconsumo), Ley 24/2013 del Sector Eléctrico, Ley 21/2013 de evaluación ambiental, RD 849/1986 (dominio público hidráulico), RDL 23/2020 y 8/2023, PLATER, normativa urbanística municipal/autonómica según emplazamiento.
- **Balance**: balance energético horario sobre año de referencia; escenarios promedio/máx/mín (histórico KRON002: 26 años, 2000–2025).
- **Pérdidas**: indicar las supuestas (histórico: 8 % genérico).

## Elementos visuales esperados
Mapa de ámbito con radio; mapa de recurso; mapa de restricciones por capas; layout con posiciones numeradas; gráficos mensual/diario de generación vs demanda; gráfico de torta de cobertura; flujo de caja acumulado; tabla de alternativas con semáforos.

## Mejoras respecto al histórico
- Resumen ejecutivo **al inicio**, con KPI, en lugar de en el medio/final.
- Un solo idioma por presentación (ENDE001 mezclaba ES y CA; había títulos como "OBJETIUS").
- Tema de color de marca en tablas y gráficos (KRON002 usaba tablas verdes y temas Office por defecto).
- Eliminar notas internas visibles ("Canviar mapa per generat amb WindPro?").
- Una idea por diapositiva y título que enuncie la conclusión cuando sea posible ("La posición 3 ofrece la mayor producción").

## Muestras
`INFORMES/04_Viabilidad_preliminar/`: `LENERGETICA_autoconsum/` (plantilla catalana de 27–32 diapositivas), `ENDESA_BonPreu/`, `KRONOSPAN_Salas/` (inglés), `KRONOSPAN_Tortosa/` (catalán/inglés, varias versiones), `AMAZON_Illescas/` (versión PDF documental). Ver [[Inventario_y_analisis]].

## Esqueleto YAML
```yaml
meta: {doc_type: posicionamiento_viabilidad, lang: es, title: "...", client: "...", code: "XXXX001", date: "AAAA-MM-DD", version: V01}
sections:
  - {id: executive_summary, blocks: [{kpis: [...]}, {p: "..."}]}
  - {id: objective, blocks: [...]}
  - {id: site_analysis, subsections: [{title: "Restricciones técnicas", blocks: [...]}]}
  - {id: technical_proposal, blocks: [...]}
  - {id: energy_analysis, blocks: [...]}
  - {id: economic_analysis, blocks: [...]}
  - {id: conclusions, blocks: [...]}
  - {id: next_steps, blocks: [...]}
```
Ejemplo completo: `examples/demo_viabilidad_es.yaml` (datos ficticios). Relacionado: [[T02_Analisis_energetico_y_economico]], [[T11_Normativa_y_urbanismo]].
