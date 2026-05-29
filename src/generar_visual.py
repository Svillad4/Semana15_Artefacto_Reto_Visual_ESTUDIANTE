"""
Generacion de recurso visual para comunicar resultados.
Este archivo contiene errores intencionales.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "produccion_fincas.csv"
OUTPUT_DIR = BASE_DIR / "resultados"
GRAPH_FILE = OUTPUT_DIR / "grafico_resultados.png"


def main():
    df = pd.read_csv(DATA_FILE)

    # ERROR INTENCIONAL 1:
    # La columna 'cantidades' no existe. Debe revisar el nombre real de la columna numerica.
    resumen = df.groupby("producto")["cantidades"].sum().sort_values(ascending=False)

    OUTPUT_DIR.mkdir(exist_ok=True)

    plt.figure(figsize=(10, 6))
    resumen.plot(kind="bar")
    plt.title("Produccion total por producto")
    plt.xlabel("Producto")
    plt.ylabel("Cantidad total")
    plt.tight_layout()

    # ERROR INTENCIONAL 2:
    # La variable GRAPH_PATH no existe. Revise el nombre correcto definido arriba.
    plt.savefig(GRAPH_PATH)
    print("Grafico generado en:", GRAPH_FILE)


if __name__ == "__main__":
    main()
