import json
import numpy as np
import statistics as stats

def rates(ruta_archivo):
    with open(ruta_archivo, 'r') as archivo:
        contenido = archivo.read()

    bloques = [b for b in contenido.strip().split('\n\n') if b]
    #b for b - creará un lista solo con los bloques no vacíos en caso de lineas vacías
    #.split('\n\n') divide el texto en partes si existe una linea en blanco entre dos diccionarios
    #contenido.strip() elimina los saltos de linea en el principio y final del archivo
    
    for i, bloque in enumerate(bloques, 1):
        try:
            data = json.loads(bloque)
            print(f"Tasa {i}: {data.get('rate')}")
        except json.JSONDecodeError as e:
            print(f"Error al decodificar bloque {i}: {e}")

rates("conversion.txt")
