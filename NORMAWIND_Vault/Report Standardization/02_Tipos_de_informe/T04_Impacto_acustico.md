---
tags: [tipo, ruido, acustica]
doc_type: impacto_acustico
formato_principal: docx
estilo: document
---
# T04 · Estudio de impacto acústico

**Propósito.** Evaluar la inmisión sonora del aerogenerador/parque sobre receptores sensibles y comprobar el cumplimiento de los límites legales; proponer medidas si no cumple. Suele integrarse como anexo del EIA/EsIA. Muestras: Cellers y Kronospan (catalán, DOCX), BAYWA Rueda Sur (español, PDF, impacto **acumulativo-sinérgico**).

## Estructura estándar (Cellers/Kronospan)
| Sección | Contenido |
|---|---|
| Introducción (`introduction`) | Marco legal del proyecto (en Cataluña: DL 16/2019, DL 24/2021) |
| Objeto (`objective`) | Evaluar inmisión potencial en receptores; determinar medidas preventivas, correctoras y compensatorias |
| Descripción del proyecto | Promotor, municipios, características de la instalación (tabla clave–valor) |
| Marco normativo (`regulatory_framework`) | Ley acústica aplicable y **tabla de valores límite** por zona de sensibilidad (Ld, Le, Ln) y altura de evaluación (4 m) |
| Análisis de la capacidad del territorio → Emplazamiento (`site_description`) | Posición UTM ETRS89, existencia de otros parques (efecto acumulativo), línea soterrada (sin efecto corona) |
| Receptores (`receivers`) | Identificación y tabla (código, tipo, distancia, zona de sensibilidad, coordenadas), mapa |
| Modelo y cálculo (`model_and_calculation`) | Software (WindPRO DECIBEL), norma **ISO 9613-2**, LWA de la turbina por modo de operación, ruido ambiente, fórmula de suma logarítmica |
| Resultados (`results`) | Tabla receptor × nivel calculado (día/tarde/noche) y mapas de isófonas |
| Evaluación (`impact_assessment`) | Comparación con límites, margen en dB(A), acumulado/sinérgico con otros parques |
| Fase de construcción (`construction_phase`) | Horario, parque de maquinaria, emisión sonora por máquina, límites de potencia acústica |
| Medidas (`mitigation`) y seguimiento (`monitoring`) | Modo de operación reducido, vigilancia acústica |
| Conclusiones (`conclusions`) | Cumple/no cumple + medidas |
| Anexos | Hojas de cálculo por receptor, certificados de emisión, mapas |

## Referencias vistas en las muestras
- Cataluña: DL 16/2019; DL 24/2021 (suspende la consulta previa). *Llei 16/2002 y Decret 176/2009 son el marco acústico catalán habitual: confirmar cita exacta en la muestra Cellers antes de reutilizar.*
- Aragón (BAYWA): **Ley 7/2010, de 18 de noviembre**, de protección contra la contaminación acústica; objetivos de calidad por tipo de área acústica (naturales, residencial, terciario, recreativo, industrial, infraestructuras) con índices Ld/Le/Ln.
- ISO 9613-2; WindPRO DECIBEL 4.1; ruido ambiente típico 40 dB día / 35 dB noche (BAYWA) – justificar siempre el valor usado.

## Elementos obligatorios
- Tabla de límites aplicables con su **fuente legal**.
- Tabla de receptores y mapa de situación.
- Tabla de resultados con margen frente al límite más restrictivo (nocturno).
- Declaración del modo de operación de la turbina considerado.

## Mejoras respecto al histórico
- Tablas en cuerpo ≥ 9 pt (las muestras usaban 7 pt).
- Títulos de sección con formato coherente (en la muestra: "Anàlisi acústicA de l'activitat").
- Mapa de isófonas siempre con leyenda, límite y receptores rotulados.
- Conclusión en un recuadro con la cifra clave (peor receptor y margen).

Muestras: `INFORMES/01_Impacto_acustico/`. Ejemplo: `examples/demo_acustico_ca.yaml`. Ver [[Inventario_y_analisis]].
