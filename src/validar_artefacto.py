from pathlib import Path
import subprocess
import sys

BASE_DIR = Path(__file__).resolve().parent.parent
REPORT_FILE = BASE_DIR / "resultados" / "reporte_resultados.txt"
GRAPH_FILE = BASE_DIR / "resultados" / "grafico_resultados.png"

print("VALIDACION DEL ARTEFACTO")
print("------------------------")

checks = []

try:
    result = subprocess.run([sys.executable, str(BASE_DIR / "src" / "main.py")], capture_output=True, text=True, timeout=20)
    checks.append(("main.py ejecuta sin errores", result.returncode == 0, result.stderr.strip()))
except Exception as error:
    checks.append(("main.py ejecuta sin errores", False, str(error)))

try:
    result = subprocess.run([sys.executable, str(BASE_DIR / "src" / "generar_visual.py")], capture_output=True, text=True, timeout=20)
    checks.append(("generar_visual.py ejecuta sin errores", result.returncode == 0, result.stderr.strip()))
except Exception as error:
    checks.append(("generar_visual.py ejecuta sin errores", False, str(error)))

checks.append(("Existe reporte_resultados.txt", REPORT_FILE.exists(), str(REPORT_FILE)))
checks.append(("Existe grafico_resultados.png", GRAPH_FILE.exists(), str(GRAPH_FILE)))

all_ok = True
for name, ok, detail in checks:
    status = "OK" if ok else "PENDIENTE"
    print(f"[{status}] {name}")
    if not ok and detail:
        print("  Detalle:", detail[:600])
    all_ok = all_ok and ok

if all_ok:
    print("\nArtefacto validado. El proyecto esta listo para entregar.")
else:
    print("\nEl artefacto aun requiere ajustes. Revise errores, bitacora y guia de depuracion.")
