from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = BASE_DIR / "data" / "produccion_fincas.csv"

print("EXPLORACION INICIAL DEL CSV")
print("---------------------------")
print("Archivo:", DATA_FILE)

df = pd.read_csv(DATA_FILE)

print("\nPrimeras 5 filas:")
print(df.head())

print("\nCantidad de filas y columnas:")
print(df.shape)

print("\nColumnas disponibles:")
for columna in df.columns:
    print("-", columna)

print("\nProductos registrados:")
print(df["producto"].value_counts())

print("\nFincas registradas:")
print(df["finca"].value_counts())
