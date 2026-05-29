from pathlib import Path
import sys

print("VERIFICACION DEL ENTORNO")
print("------------------------")
print("Version de Python:", sys.version)
print("Carpeta actual:", Path.cwd())

try:
    import pandas as pd
    print("pandas instalado:", pd.__version__)
except Exception as error:
    print("No se pudo importar pandas.")
    print("Solucion sugerida: pip install -r requirements.txt")
    print("Detalle:", error)

try:
    import matplotlib
    print("matplotlib instalado:", matplotlib.__version__)
except Exception as error:
    print("No se pudo importar matplotlib.")
    print("Solucion sugerida: pip install -r requirements.txt")
    print("Detalle:", error)
