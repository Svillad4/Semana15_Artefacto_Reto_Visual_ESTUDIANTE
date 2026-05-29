# Semana 15 - Artefacto del entorno
## Reto colaborativo con comunicación visual de resultados

Este proyecto base forma parte de la actividad **Semana 15: Artefacto del entorno**.
La finalidad es que el equipo convierta una práctica guiada en un producto ejecutable, organizado y documentado.

## Contexto del reto

Una comunidad rural necesita comprender los resultados de producción de varias fincas. El equipo debe crear una mini-solución que:

1. lea datos desde un archivo CSV;
2. calcule resultados principales;
3. genere un reporte técnico en texto;
4. produzca un recurso visual para comunicar los resultados;
5. documente las pruebas realizadas;
6. registre los roles del equipo y los aportes de cada integrante.

## Importante

Los archivos `src/main.py` y `src/generar_visual.py` contienen **errores intencionales**. No están dañados por accidente: el reto consiste en abrirlos, leerlos, ejecutar los comandos, interpretar los mensajes de error, corregirlos y documentar el proceso.

## Estructura del proyecto

```text
Semana15_Artefacto_Reto_Visual_ESTUDIANTE/
├── README.md
├── requirements.txt
├── data/
│   └── produccion_fincas.csv
├── src/
│   ├── 00_verificar_entorno.py
│   ├── 01_explorar_datos.py
│   ├── main.py
│   ├── generar_visual.py
│   └── validar_artefacto.py
├── resultados/
├── evidencias/
│   ├── bitacora.md
│   ├── pruebas.md
│   └── roles_equipo.md
├── presentacion/
│   └── resumen_visual.md
├── plantillas/
│   └── README_FINAL_PLANTILLA.md
└── docs/
    ├── GUIA_ESTUDIANTE.md
    ├── explicacion_bloque_a_bloque.md
    ├── guia_depuracion.md
    ├── guia_recursos_visuales.md
    ├── checklist_entrega.md
    ├── rubrica.md
    └── descripcion_moodle.txt
```

## Instalación recomendada

Abre esta carpeta en Visual Studio Code. Luego abre la terminal integrada y ejecuta:

```bash
python --version
```

Si Python está instalado, instala las dependencias:

```bash
pip install -r requirements.txt
```

## Comandos del laboratorio

Ejecuta en orden:

```bash
python src/00_verificar_entorno.py
python src/01_explorar_datos.py
python src/main.py
python src/generar_visual.py
python src/validar_artefacto.py
```

Si algún comando falla, lee el mensaje de error, identifica la causa y registra el ajuste en `evidencias/bitacora.md`.

## Producto final esperado

El equipo debe entregar un ZIP final que incluya:

- proyecto ejecutable;
- README final claro;
- reporte generado en `resultados/reporte_resultados.txt`;
- gráfico generado en `resultados/grafico_resultados.png`;
- evidencias de pruebas;
- registro de roles;
- resumen visual de resultados;
- bitácora de errores y ajustes.
