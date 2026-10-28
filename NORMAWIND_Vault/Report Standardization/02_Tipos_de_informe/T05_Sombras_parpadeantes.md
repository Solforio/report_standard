---
tags: [tipo, sombras, shadow-flicker]
doc_type: sombras_parpadeantes
formato_principal: docx
estilo: document
---
# T05 · Estudio de sombras parpadeantes (shadow flicker)

**Propósito.** Evaluar las horas de sombra proyectada por el rotor sobre receptores fijos (viviendas o, en autoconsumo industrial, ventanas/puestos de trabajo) y proponer medidas. Muestra de referencia: **Amazon MAD7** (PDF, 16 págs.; el DOCX de Kronospan reutiliza el mismo texto).

## Estructura estándar (muestra MAD7)
| Sección | Contenido |
|---|---|
| Objeto y alcance (`objective`) | Turbina, emplazamiento, receptores considerados y por qué; hipótesis conservadoras (sin vidrio atenuante, sin toldos) |
| Normativa aplicable (`regulatory_framework`) | No hay límite legal en España. Se toman referencias: indicaciones alemanas, IWEA 2019, Connecticut, Japón → **30 h/año** (máx., peor caso) u **8 h/año** (caso real) y/o **30 min/día**. Salud: epilepsia fotosensible (3–60 Hz) |
| Descripción del emplazamiento (`site_description`) | Ubicación, entorno, fotomontaje, plano |
| Recurso eólico (`wind_resource`) | Sectores dominantes, rosa de energía (para horas de operación) |
| Datos de entrada (`input_data`) | Topografía, aerogenerador (tabla), obstáculos, **receptores** (ventanas A1…E, caseta; altura, anchura, orientación, cota) |
| Metodología (`methodology`) | Módulo SHADOW de WindPRO 4.0: simulación del sol minuto a minuto durante un año. Casos: **Worst case**, **Real case** (probabilidad de horas de sol y operación), **Sombras efectivas** (por turno/horario laboral) |
| Resultados (`results`) | Parámetros estadísticos (horas de sol por mes, distribución de viento por sector), mapa de sombras, tabla por receptor (h/año, días, máx. min/día) |
| Evaluación del impacto (`impact_assessment`) | Salud de las personas; molestias a trabajadores (factores atenuantes: iluminación, posición, obstáculos, orientación) |
| Conclusiones (`conclusions`) y medidas (`mitigation`) | **Pasivas** (sobre ventanas: vinilos, cortinas/estores, láminas…) y **activas** (sobre trabajadores o sobre la turbina: parada programada) |
| Programa de seguimiento (`monitoring`) | Verificación tras la puesta en marcha |

## Datos de entrada necesarios
Coordenadas y altura de buje/diámetro de rotor, receptores con geometría y orientación, serie de horas de sol (estación meteorológica), distribución de viento por sector, horarios laborales, umbrales de referencia.

## Elementos visuales
Fotomontaje, plano de ubicación, tabla de receptores, calendario de sombras por receptor (mes × hora), mapa de isolíneas de horas/año, gráficos mensuales.

## Criterios de resultado (plantilla de frase)
"El receptor **{id}** recibe **{x} h/año** en el caso real, **{superior/inferior}** al umbral de referencia de **8 h/año**" + efecto de atenuantes + medida propuesta.

## Mejoras respecto al histórico
- Resumen con una tabla "receptor × h/año × cumple" antes del detalle.
- Separar claramente *potencial* (worst case), *real* y *efectivo*.
- Eliminar referencias a otro proyecto (el DOCX de Kronospan conserva texto de Amazon/MAD7: [[Hallazgos_de_auditoria]]).
- Terminología catalana pendiente de validación (*ombres parpellejants* / *efecte estroboscòpic*): [[Glosario_trilingue]].

Muestras: `INFORMES/02_Sombras_parpadeantes/`. Relacionado: [[T03_Recurso_eolico_y_produccion]], [[T06_Estudio_visual]].
