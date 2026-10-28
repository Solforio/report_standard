---
tags: [tipo, terrenos, propietarios, rgpd]
doc_type: terrenos_propietarios
formato_principal: docx
estilo: document
confidencial: true
---
# T10 · Terrenos y propietarios

**Propósito.** Registrar fincas y propietarios afectados por cada aerogenerador y el estado de negociación. **Documento interno**, no se entrega a terceros sin depurar. Muestra: *Informe propietaris* (Galatea).

## Estructura (muestra)
Una **ficha por finca**, agrupadas por aerogenerador (G1, G2…):

| Campo | Ejemplo / contenido |
|---|---|
| Propietario | Razón social o nombre |
| Finca | Referencia (polígono/parcela, nº de finca) |
| Contacto | Persona y teléfono |
| Tipo de afección | % de volumen, cimentación, plataforma, zanja, camino |
| Estado | Sin contactar / contactado-negociando / acuerdo / rechazo |
| Ofertado | €/año (renta) |
| Comentarios | Condiciones planteadas |

Cierra con un **resumen**: nº de fincas, % con acuerdo, riesgos, próximos pasos (`next_steps`).

## Protección de datos (RGPD / LOPDGDD)
- Contiene **datos personales** (nombres, teléfonos). Marcar `confidential: true`, restringir a quien lo necesita y no incluir en entregas a clientes o administraciones sin anonimizar.
- Para entregas externas, generar la versión **solo con referencias catastrales y estado**, sin contactos ni importes.

## Mejoras respecto al histórico
La muestra era un texto plano sin estructura; ahora es tabla por finca con estados normalizados y resumen cuantitativo.

Muestras: `INFORMES/12_Terrenos_y_propietarios/`. Ver [[Estilo_de_redaccion]].
