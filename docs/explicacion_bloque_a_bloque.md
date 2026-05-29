# Explicación bloque a bloque

## Bloque 1: Importaciones

Los scripts usan `Path` para trabajar con rutas de archivos, `pandas` para leer y agrupar datos, y `matplotlib` para crear gráficos.

## Bloque 2: Rutas del proyecto

La variable `BASE_DIR` identifica la carpeta principal del proyecto. Desde ahí se construyen rutas hacia `data/`, `resultados/` y otros archivos.

Trabajar con rutas bien definidas evita errores cuando el proyecto se abre desde otro equipo.

## Bloque 3: Carga de datos

El archivo CSV está en `data/produccion_fincas.csv`. El script debe leerlo con `pd.read_csv(DATA_FILE)`.

Si aparece un error de archivo no encontrado, revisa:

- nombre de la carpeta;
- nombre del archivo;
- ubicación real del CSV;
- variable usada en el código.

## Bloque 4: Agrupación de datos

`groupby()` permite agrupar los registros por producto, finca o zona. Después se usa `sum()` o `mean()` para calcular totales o promedios.

Ejemplo:

```python
df.groupby("producto")["cantidad"].sum()
```

Esto significa: agrupar por producto y sumar la columna cantidad.

## Bloque 5: Reporte de texto

El reporte convierte los resultados en texto legible. Debe guardarse en `resultados/reporte_resultados.txt`.

## Bloque 6: Gráfico

El gráfico ayuda a comunicar resultados. En esta actividad se recomienda un gráfico de barras para comparar producción total por producto.

## Bloque 7: Validación

`validar_artefacto.py` revisa si los scripts ejecutan y si existen los archivos finales. Es una prueba rápida antes de entregar.
