---
tags: [flujo, mantenimiento]
---
# Ampliar y mantener el sistema

## Añadir un tipo de informe
1. Crear la ficha en `02_Tipos_de_informe/` copiando una existente (estructura, datos, criterios, mejoras, muestras).
2. Añadir el tipo en `data/report_types.yaml` (`primary`, `formats`, `style`, `sections` con `*` en las obligatorias).
3. Añadir su nombre en `data/strings.yaml` → `types` (es/en/ca).
4. Si necesita secciones nuevas → `strings.yaml` → `sections` con las tres traducciones.
5. Crear un ejemplo en `examples/` y generarlo en los 3 idiomas.
6. Enlazarlo en [[00_Mapa_de_tipos]].

## Añadir o corregir un término
Editar [[Glosario_trilingue]]; si es una etiqueta de plantilla (título de sección, "Versión"…), **también** `data/strings.yaml`.

## Cambiar la marca
Colores y fuente: `scripts/nwcommon.py` y [[Identidad_visual]]. Logos: `assets/logos/`.

## Pendientes y mejoras previstas
- [ ] **Validar terminología catalana** marcada (¿) con el equipo.
- [x] ~~Portada con fotografía~~: hecho en v2 (foto B/N del histórico KRON002; confirmar derechos de uso). Fotos propias vía `cover_image`.
- [x] ~~Abadi Extra Light~~: adoptada en PPTX (DOCX/HTML siguen en Calibri; valorar unificar).
- [ ] Láminas de mapa a pantalla completa y tablas con bandas de color por bloque (como KRON002).
- [ ] **Gráficos nativos** en PPTX (editables) en lugar de imágenes.
- [ ] **HTML interactivo** para visor de fotomontajes y calendario de sombras.
- [ ] **XLSX** como quinto formato (historial de tramitación, tablas de resultados).
- [ ] **Plantilla `.dotx`/`.potx`** corporativa exportada del generador para quien prefiera escribir a mano.
- [ ] Confirmar con el equipo **condiciones de uso del logo EMD**.
- [ ] Confirmar **tipografía corporativa** definitiva (Calibri se eligió por ser la dominante en los PDF y estar disponible en todos los equipos).
- [ ] Ampliar la biblioteca de muestras con informes recientes de cada tipo y revisar los hallazgos de [[Hallazgos_de_auditoria]].
- [ ] Definir **flujo de validación** (quién valida qué tipo antes de enviar).

## Versionado del sistema
Anotar aquí cada cambio relevante.
| Fecha | Cambio |
|---|---|
| 2026-10-28 | Versión 1: 11 tipos, 4 formatos, 3 idiomas, vault inicial |
| 2026-10-28 | PPTX layout v2: calcado de KRON002 (banda gris con versalitas, portada y contraportada con foto B/N y misma retícula, tablas y callouts más ligeros, separadores de sección). Vault con capturas en `Adjuntos/` y copia en Notion. `build_report.py` reintenta la exportación de Office si falla |
| 2026-10-28 | PPTX en fuente Abadi Extra Light; foto de portada y contraportada del histórico para todos los informes |
| 2026-10-28 | PPTX: logo NORMAWIND horizontal girado 90° en el borde derecho de portada/contraportada (sustituye a la barra taupe; layout tomado del T02 retocado por el equipo) y logo pequeño en el pie de todas las diapositivas |
