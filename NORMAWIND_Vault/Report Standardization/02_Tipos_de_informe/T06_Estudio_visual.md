---
tags: [tipo, visual, fotomontaje]
doc_type: estudio_visual
formato_principal: pdf
estilo: document
---
# T06 · Estudio de impacto visual (fotomontajes)

**Propósito.** Mostrar cómo se verá el aerogenerador desde puntos representativos del entorno (viviendas, caminos, carreteras, núcleos urbanos) mediante fotografías y fotomontajes. Anexo habitual del EIA. Muestra: **El Molí de Calero** (Anexo 11, 16 págs., febrero 2026).

## Estructura (muestra Calero)
1. Portada con control de versión/autores/validación.
2. **Ficha de metodología**: cámara (modelo, distancia focal), fecha/hora de las fotos, software.
3. **Lista de puntos de vista** (PV01…PV10) con nombre y coordenadas ETRS89.
4. **Una ficha por punto de vista**: nombre, **distancia a la turbina (km)**, dirección de cámara, fecha y hora de la foto, *vista existente* + *fotomontaje* + *plano de ubicación*.
5. Aviso legal: un fotomontaje no puede reproducir con exactitud la realidad (luz, meteorología, estaciones, resolución; no muestra movimiento ni reflejos de las palas).
6. (Recomendado) Cuadro-resumen de visibilidad y conclusiones.

## Mapeo a secciones
`objective` · `site_description` · `viewpoints` (una subsección por PV) · `impact_assessment` · `conclusions` · `annexes`.

## Reglas
- Misma focal y encuadre en vista existente y fotomontaje; indicar focal equivalente (la muestra decía "3,6 m": debe ser **mm**).
- Altura de turbina simulada = altura total (buje + radio de rotor).
- Numeración PV consistente con el plano y la tabla de coordenadas.
- Cada ficha ocupa una página (A4 apaisado recomendable para el par foto/fotomontaje).

## Cuándo ofrecer HTML
Visor con selector de puntos de vista, comparación antes/después con deslizador y mapa. Útil para reuniones con ayuntamientos.

## Mejoras respecto al histórico
- Índice funcional (el PDF histórico tenía marcadores incorrectos).
- Tabla resumen de distancias y visibilidad.
- Texto legal estandarizado en los tres idiomas.

Muestras: `INFORMES/07_Estudios_visuales/`. Relacionado: [[T05_Sombras_parpadeantes]].
