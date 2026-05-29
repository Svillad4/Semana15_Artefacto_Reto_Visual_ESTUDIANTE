# Guía del estudiante
## Semana 15: Artefacto del entorno
### Mini-solución colaborativa con comunicación visual de resultados

## 1. Qué vas a construir

En esta actividad vas a convertir un proyecto base en un **artefacto técnico ejecutable**. Esto significa que tu entrega no será solamente una captura de pantalla o una respuesta escrita. Debes entregar un proyecto que otra persona pueda abrir, leer, ejecutar y comprender.

El artefacto debe resolver un reto contextual: una comunidad rural necesita revisar datos de producción de varias fincas y comunicar los resultados de forma clara mediante un reporte y un recurso visual.

## 2. Qué aprenderás

Al completar esta actividad aprenderás a:

- organizar un proyecto por carpetas;
- usar Visual Studio Code como entorno de trabajo;
- ejecutar scripts desde la terminal;
- leer datos desde un CSV;
- corregir errores de rutas, nombres de columnas y variables;
- generar un reporte de resultados;
- crear un gráfico para comunicar información;
- registrar pruebas y errores;
- distribuir roles de trabajo en equipo;
- preparar una explicación visual del resultado.

## 3. Ruta de trabajo

Sigue este orden:

1. Abre el proyecto en VS Code.
2. Lee este documento completo.
3. Revisa `README.md`.
4. Ejecuta `python src/00_verificar_entorno.py`.
5. Ejecuta `python src/01_explorar_datos.py`.
6. Ejecuta `python src/main.py` y observa el error.
7. Corrige los errores de `main.py`.
8. Ejecuta `python src/generar_visual.py` y observa el error.
9. Corrige los errores de `generar_visual.py`.
10. Ejecuta `python src/validar_artefacto.py`.
11. Completa la bitácora, las pruebas y los roles del equipo.
12. Completa el resumen visual en `presentacion/resumen_visual.md`.
13. Actualiza el README final.
14. Comprime el proyecto y entrégalo en Moodle.

## 4. Por qué el proyecto tiene errores

Los errores son parte de la actividad. El propósito no es que todo funcione desde el inicio, sino que aprendas a diagnosticar. En programación profesional, los mensajes de error no son enemigos: son pistas. Un buen estudiante técnico debe aprender a leerlos, identificar la causa y aplicar un ajuste.

## 5. Evidencias mínimas

Debes entregar evidencia de:

- comandos ejecutados;
- errores encontrados;
- correcciones aplicadas;
- reporte generado;
- gráfico generado;
- roles de equipo;
- interpretación de resultados.

## 6. Resultado esperado

Al final deben existir estos archivos:

```text
resultados/reporte_resultados.txt
resultados/grafico_resultados.png
evidencias/bitacora.md
evidencias/pruebas.md
evidencias/roles_equipo.md
presentacion/resumen_visual.md
README.md actualizado
```

## 7. Recomendación técnica

No corrijas al azar. Primero lee el error, luego revisa el archivo CSV con `01_explorar_datos.py`, identifica el nombre correcto de columnas y variables, aplica el cambio y ejecuta nuevamente.
