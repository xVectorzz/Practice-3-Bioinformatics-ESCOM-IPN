# Práctica 3: Cálculo de Centroides y Centro de Masa (PDB)

Este script calcula el centroide y el centro de masa de las cadenas de una proteína a partir del archivo `1JMQ.pdb`, utilizando los pesos atómicos. 

## Instrucciones de uso

Asegúrate de tener `Practica3.py` y `1JMQ.pdb` en tu carpeta. Abre tu terminal y corre estos comandos en orden para preparar el entorno, instalar lo necesario y ejecutar el script:

**En Ubuntu (WSL / Linux):**
```bash
# Crear entorno, activar, instalar dependencias y ejecutar
python3 -m venv bioenv
source bioenv/bin/activate
pip install periodictable
python3 Practica3.py
```

**En Windows (CMD):**
```cmd
# Crear entorno, activar, instalar dependencias y ejecutar
python -m venv bioenv
bioenv\Scripts\activate
pip install periodictable
python Practica3.py
```
