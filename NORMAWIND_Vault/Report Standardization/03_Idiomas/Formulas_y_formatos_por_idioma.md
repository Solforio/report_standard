---
tags: [idiomas, formato]
---
# Fórmulas y formatos por idioma

## Números, fechas y unidades
| | Español | Català | English |
|---|---|---|---|
| Decimal / millares | `13.070,5` | `13.070,5` | `13,070.5` |
| Porcentaje | `13,7 %` | `13,7 %` | `13.7%` |
| Moneda | `9.161.360 €` | `9.161.360 €` | `€9,161,360` |
| Fecha numérica | `28/10/2026` | `28/10/2026` | `28/10/2026` (dd/mm/aaaa, sin ambigüedad: se imprime siempre así) |
| Fecha larga (cartas) | 28 de octubre de 2026 | 28 d'octubre de 2026 | 28 October 2026 |
| Unidades | `80 m` · `5 MW` · `4,081 GWh/año` | `80 m` · `5 MW` · `4,081 GWh/any` | `80 m` · `5 MW` · `4.081 GWh/year` |

> [!warning] Hallazgo en el histórico
> El *site assessment* en inglés (MAD07) escribía `4.081` GWh/año y `1.855` horas equivalentes con el mismo punto: en inglés el punto es decimal, así que "1.855 h" se leería como 1,855 h. Regla: **el formato numérico sigue al idioma del informe** y las tablas importadas de Excel se convierten antes de insertarse.

## Fórmulas fijas
| Función | Español | Català | English |
|---|---|---|---|
| Objeto | Este documento tiene por objeto… | Aquest document té per objecte… | This document aims to… |
| Elaboración | Informe elaborado por NORMAWIND S.L. | Informe elaborat per NORMAWIND S.L. | Report prepared by NORMAWIND S.L. |
| Primera versión | Primera versión | Primera versió | First version |
| Hipótesis | Se ha considerado la hipótesis de… | S'ha considerat la hipòtesi de… | The assumption of … has been considered. |
| Cumple | cumple con el límite de… | compleix amb el límit de… | complies with the limit of … |
| Recomendación | Se recomienda… | Es recomana… | It is recommended that… |
| Cierre de carta | Quedamos a su disposición para cualquier aclaración. | Restem a la seva disposició per a qualsevol aclariment. | We remain at your disposal for any clarification. |
| Fuente | Fuente: elaboración propia | Font: elaboració pròpia | Source: own elaboration |
| Confidencial | Confidencial. Uso exclusivo del destinatario. | Confidencial. Ús exclusiu del destinatari. | Confidential. For the addressee only. |

## Aviso estándar de fotomontajes
- **CA** (original de la muestra Calero): *Una visualització no pot mostrar amb un 100% d'exactitud com serà exactament l'aerogenerador en la realitat a causa de factors com ara: diferents condicions de llum, meteorologia i estacions que varien amb el temps, així com la resolució de la imatge. Una imatge estàtica no pot transmetre el moviment de la turbina, ni el parpelleig o el reflex del sol sobre les pales de la turbina mentre es mouen.*
- **ES**: *Una visualización no puede mostrar con total exactitud cómo será el aerogenerador en la realidad debido a factores como las distintas condiciones de luz, la meteorología y las estaciones, así como la resolución de la imagen. Una imagen estática no puede transmitir el movimiento de la turbina ni el parpadeo o el reflejo del sol sobre las palas en movimiento.*
- **EN**: *A visualisation cannot show with complete accuracy how the wind turbine will look in reality, owing to factors such as varying light conditions, weather and seasons, and image resolution. A still image cannot convey the movement of the turbine, nor the flicker or sun reflections on the moving blades.*

## Cabecera de la tabla de versiones por idioma
Ver `data/strings.yaml` (etiquetas `version`, `date`, `changes`, `authors`, `validated_by`…). Cualquier cambio de etiqueta se hace **solo allí**.

## Idioma por tipo de cliente (orientativo)
Administración catalana → CA · administración estatal / otras CCAA → ES · clientes internacionales (Amazon, BAYWA, Kronospan técnico) → EN o ES según contrato. **Preguntar siempre** ([[Preguntas_iniciales]]).
