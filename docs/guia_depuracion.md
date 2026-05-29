# Guía de depuración

## Error 1: NameError

Significa que el código usa una variable que no existe o está mal escrita.

Ejemplo:

```text
NameError: name 'DATAFILE' is not defined
```

Pista: revisa si la variable correcta se llama `DATA_FILE`.

## Error 2: KeyError

Significa que intentas usar una columna que no existe en el DataFrame.

Ejemplo:

```text
KeyError: 'cantidad_total'
```

Pista: ejecuta `python src/01_explorar_datos.py` para ver las columnas reales del CSV.

## Error 3: TypeError al guardar reporte

Puede ocurrir si una función no retorna texto y luego se intenta guardar `None`.

Pista: revisa si `construir_reporte()` tiene un `return`.

## Error 4: Archivo visual no generado

Puede ocurrir si guardas con una variable incorrecta.

Pista: revisa si la variable correcta se llama `GRAPH_FILE`.

## Método profesional de corrección

1. Ejecuta el script.
2. Copia o resume el error en la bitácora.
3. Identifica el archivo y línea donde ocurre.
4. Corrige solo una cosa a la vez.
5. Ejecuta de nuevo.
6. Registra el ajuste aplicado.
