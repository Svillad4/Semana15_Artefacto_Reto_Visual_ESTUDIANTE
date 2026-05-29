"""
Semana 15 - Artefacto del entorno
Reto colaborativo: comunicacion de resultados con recursos visuales

Este archivo contiene errores intencionales.
El equipo debe corregirlos, ejecutar el programa y documentar los ajustes.
"""

from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "produccion_fincas.csv"
OUTPUT_DIR = BASE_DIR / "resultados"
REPORT_FILE = OUTPUT_DIR / "reporte_resultados.txt"


def cargar_datos():
    """Carga el archivo CSV del proyecto."""
    # ERROR INTENCIONAL 1:
    # La ruta usa una variable mal escrita. Revise el nombre correcto definido arriba.
    df = pd.read_csv(DATAFILE)
    return df


def calcular_resumen(df):
    """Calcula indicadores principales para comunicar resultados."""
    # ERROR INTENCIONAL 2:
    # La columna 'cantidad_total' no existe en el CSV. Explore las columnas reales.
    total_por_producto = df.groupby("producto")["cantidad_total"].sum().sort_values(ascending=False)

    # ERROR INTENCIONAL 3:
    # La columna 'fincas' no existe. Revise si el nombre correcto está en singular o plural.
    total_por_finca = df.groupby("fincas")["cantidad"].sum().sort_values(ascending=False)

    promedio_por_zona = df.groupby("zona")["cantidad"].mean().sort_values(ascending=False)

    return total_por_producto, total_por_finca, promedio_por_zona


def construir_reporte(total_por_producto, total_por_finca, promedio_por_zona):
    """Construye un texto de reporte para guardar y presentar."""
    lineas = []
    lineas.append("REPORTE DE RESULTADOS - SEMANA 15")
    lineas.append("Reto colaborativo y comunicacion visual")
    lineas.append("=" * 55)

    lineas.append("\n1. Total producido por producto")
    lineas.append(str(total_por_producto))

    lineas.append("\n2. Total producido por finca")
    lineas.append(str(total_por_finca.head(8)))

    lineas.append("\n3. Promedio de cantidad por zona")
    lineas.append(str(promedio_por_zona))

    lineas.append("\n4. Interpretacion para la presentacion")
    lineas.append("El equipo debe explicar que producto o finca obtuvo mayor produccion,")
    lineas.append("que grafico ayuda a comunicar mejor el resultado y que decision podria")
    lineas.append("tomar la comunidad con base en estos datos.")

    # ERROR INTENCIONAL 4:
    # Falta retornar el texto final. Revise que debe devolver la funcion.


def guardar_reporte(reporte):
    """Guarda el reporte en la carpeta resultados."""
    OUTPUT_DIR.mkdir(exist_ok=True)
    REPORT_FILE.write_text(reporte, encoding="utf-8")
    print("Reporte generado en:", REPORT_FILE)


def main():
    df = cargar_datos()
    total_por_producto, total_por_finca, promedio_por_zona = calcular_resumen(df)
    reporte = construir_reporte(total_por_producto, total_por_finca, promedio_por_zona)
    guardar_reporte(reporte)
    print("\nResumen generado correctamente.")


if __name__ == "__main__":
    main()
