# Bitácora de errores y ajustes

| Nº | Archivo | Error encontrado | Mensaje o pista del error | Causa identificada | Ajuste aplicado | Resultado |
|---:|---|---|---|---|---|---|
| 1 | src/main.py | Variable mal escrita | NameError: name 'DATAFILE' is not defined | Se usó DATAFILE en lugar de DATA_FILE | Reemplazado por DATA_FILE | Se leyó el CSV correctamente |
| 2 | src/main.py | Nombre de columna incorrecto | KeyError: 'Column not found: cantidad_total' | Se usó cantidad_total en lugar de cantidad | Cambiado a cantidad | Se calculó el total por producto |
| 3 | src/main.py | Nombre de columna incorrecto | KeyError: 'Column not found: fincas' | Se usó fincas en lugar de finca | Cambiado a finca | Se calculó el total por finca |
| 4 | src/main.py | Retorno faltante | TypeError: data must be str, not NoneType | La función no devolvía el texto del reporte | Agregado return "\n".join(lineas) | Se generó el reporte |
| 5 | src/generar_visual.py | Nombre de columna incorrecto | KeyError: 'Column not found: cantidades' | Se usó cantidades en lugar de cantidad | Cambiado a cantidad | Se calculó el gráfico |
| 6 | src/generar_visual.py | Variable mal escrita | NameError: name 'GRAPH_PATH' is not defined | Se usó GRAPH_PATH en lugar de GRAPH_FILE | Cambiado a GRAPH_FILE | Se guardó el gráfico |

## Reflexión técnica

Aprendí a leer mensajes de error y usar nombres de variables y columnas correctos.

¿Qué comando te ayudó más a validar el proyecto?

python src/main.py y python src/generar_visual.py

¿Qué mejorarías si tuvieras más tiempo?

Mejoraría la explicación del código y revisaría más datos del CSV.
