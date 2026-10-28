#!/usr/bin/env bash
# Regenera los 11 informes facsímil (DOCX, PPTX, PDF) en FACSIMILES/. Ejecutar desde la raíz del proyecto.
# no se detiene si un archivo está abierto en Word/PowerPoint: sigue con el resto
E=.claude/skills/normawind-reports/examples
B="python -I .claude/skills/normawind-reports/scripts/build_report.py"
OUT=FACSIMILES
run() { $B "$1" --formats "$3" --out $OUT --name "$2" || echo "FALLO: $2"; }
run $E/demo_viabilidad_es.yaml            T01_Posicionamiento_viabilidad_ES docx,pptx,pdf
run $E/facsimiles/T02_energetico_economico_ca.yaml T02_Energetico_economico_CA docx,pptx,pdf
run $E/facsimiles/T03_recurso_eolico_en.yaml  T03_Recurso_eolico_EN  docx,pptx,pdf
run $E/demo_acustico_ca.yaml              T04_Impacto_acustico_CA   docx,pptx,pdf
run $E/facsimiles/T05_sombras_es.yaml     T05_Sombras_parpadeantes_ES docx,pptx,pdf
run $E/facsimiles/T06_visual_ca.yaml      T06_Estudio_visual_CA     docx,pptx,pdf
run $E/facsimiles/T07_accesos_es.yaml     T07_Accesos_transporte_ES docx,pptx,pdf
run $E/demo_respuesta_en.yaml             T08_Respuesta_requerimiento_EN docx,pptx,pdf
run $E/facsimiles/T09_alternativas_ca.yaml T09_Alternativas_CA      docx,pptx,pdf
run $E/facsimiles/T10_terrenos_es.yaml    T10_Terrenos_propietarios_ES docx,pptx,pdf
run $E/facsimiles/T11_normativa_ca.yaml   T11_Normativa_urbanismo_CA docx,pptx,pdf
