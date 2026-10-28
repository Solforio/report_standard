---
tags: [plantilla]
---
# Plantilla de contenido en blanco

Copiar el bloque a un archivo `.yaml`, rellenar y generar ([[Esquema_YAML]]). Quitar las secciones que no apliquen (conservar las obligatorias del tipo).

```yaml
meta:
  doc_type: posicionamiento_viabilidad   # ver 00_Mapa_de_tipos
  lang: es                               # es | ca | en
  title: ""
  short_title: ""
  subtitle: ""
  client: ""
  project: ""
  location: ""
  code: ""                               # p. ej. KRON002
  date: "AAAA-MM-DD"
  version: V01
  authors: []
  validated_by: ""
  # client_logo: ruta/logo.png
  # powered_by_emd: true
  # draft: true

sections:
  - id: executive_summary
    blocks:
      - kpis:
          - {label: "", value: "", unit: ""}
      - p: "[PENDIENTE]"
  - id: objective
    blocks:
      - p: "[PENDIENTE]"
  - id: conclusions
    blocks:
      - bullets: ["[PENDIENTE]"]
```
