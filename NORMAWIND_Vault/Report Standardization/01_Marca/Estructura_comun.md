---
tags: [marca, estructura]
---
# Estructura común de todos los informes

Deriva del patrón que ya usaban los informes históricos (portada → revisiones → índice → cuerpo) y lo hace uniforme. Ver [[Hallazgos_de_auditoria]] para lo que se ha corregido.

## Piezas fijas (DOCX / PDF)
1. **Portada**: logo NORMAWIND · etiqueta del tipo de informe · título · subtítulo · cliente, proyecto, emplazamiento, referencia, versión, fecha · (logo del cliente).
2. **Control de revisiones**: tabla *Versión / Fecha / Cambios* + *Autor(es) / Validado por* + ficha *Nombre del documento, Referencia, Versión, Fecha*. (En el histórico: "Versió/Data/Descripció · Autors/Validació · Nom del document/Versió/Codi".)
3. **Índice** automático (niveles 1–2, con números de página).
4. **Cuerpo** con secciones numeradas (1, 1.1). Sin portada/índice en las cartas ([[T08_Respuesta_a_requerimiento]]).
5. **Cabecera**: logo (izq.) + título corto (dcha.) con filete azul. **Pie**: `código · título corto` + `Página X de Y` + aviso de confidencialidad.
6. **Anexos** al final, numerados "Anexo 1…".

## Piezas fijas (PPTX, 16:9)
1. **Portada** clara con foto B/N a la derecha: tipo de informe, título, proyecto, fecha, cliente (+ logo) y logo NORMAWIND.
2. Diapositiva de **control de revisiones** (misma tabla que el DOCX).
3. **Índice** numerado.
4. Diapositivas de contenido: **banda gris con título en versalitas** + contenido + pie discreto (código y nº). Separadores de sección con banda a media altura.
5. **Contraportada con la misma retícula que la portada** (foto a la derecha, logo y contacto a la izquierda).

![[pptx_portada.png]]
![[pptx_contraportada.png]]

Detalle de coordenadas y reglas en [[PPTX]].

## Numeración y rotulado
- Secciones: `1`, `1.1` (máx. 3 niveles; el tercero sin número en DOCX).
- Figuras y tablas numeradas correlativamente en todo el documento: *Figura 3. …* (pie) y *Tabla 2. …* (encima). Cada una con **fuente** si no es elaboración propia.
- Toda tabla y figura se **cita en el texto** antes de aparecer.
- Unidades con espacio fino: `4,081 GWh/año`, `80 m`, `5 MW`. Símbolos SI. Ver [[Formulas_y_formatos_por_idioma]].

## Identificación del documento
- **Referencia/código**: `CLIENTE###` del proyecto (AMAZ001, ESTA005, KRON002, ENDE001, SOME002, ENEL001…). Los informes de consultoría para terceros pueden llevar además el consecutivo interno `03-0NN-25` (p. ej. `03-018-25`).
- **Nombre de archivo** (lo genera la skill): `AAAAMMDD_CÓDIGO_Titulo-corto_IDIOMA.ext`
  Ej.: `20261028_KRON002_Viabilidad-eolica-autoconsumo_ES.docx`
- **Versión**: `V01`, `V02`… (borradores `V01-D1`). Cada versión nueva añade fila en el control de revisiones.
- **Autor / validación**: iniciales o nombre completo del autor y de quien valida (histórico: "M.A., M.B. / V.C."). Nunca sin validación antes de enviar al cliente.

## Elementos que no pueden faltar (todos los tipos)
- Objeto y alcance claros en la primera página de contenido.
- Datos de partida y su origen.
- Conclusiones que respondan al objeto (con cifras clave).
- Fecha, versión y validación.

## Elementos recomendados (mejora sobre el histórico)
- **Resumen ejecutivo** al inicio con 3–5 cifras clave (tarjetas KPI) y la conclusión en una frase.
- **Llamadas (callouts)** para riesgos, hipótesis críticas y conclusiones; no más de 2 por sección.
- **Hipótesis y limitaciones** explícitas (p. ej. fotomontajes, modelos de ruido, precios de mercado).
- **Próximos pasos** con responsables cuando el informe es de viabilidad.
