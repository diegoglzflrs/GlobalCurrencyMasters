import os
import sys
import subprocess
import requests
import json
apikey = '7a86521fff0242e4b35bf70ee3696f80'

def open_in_idle(file):
    idle_path = os.path.join(sys.base_prefix, 'Lib', 'idlelib', 'idle.pyw')
    command = [sys.executable, idle_path, file]
    subprocess.Popen(command)

def menu():
    print("""###Global###Currency###Masters###
###           ###                ###              ###
###           ###                ###              ###
###           ###                ###              ###
###           ###                ###              ###
1. Consultar tipos de monedas"
2. Convertir fuente a blanco
3. Consultar tasas de conversiones recientes
4. Salir""")

def consultarMonedas():
    url = f'https://api.currencyfreaks.com/v2.0/supported-currencies'
    buscar = input("Ingrese el código de moneda que desea buscar: ").upper()
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        texto_json = json.dumps(datos, indent=2)
        with open("consulta.txt", "w") as archivo:
            archivo.write(texto_json)
        for codigo, nombre in datos.items(): 
            if buscar in codigo or buscar in nombre:
                print("Si existe")
            else:
                print("No existe")
    else:
        print(f"Error: No se pudo encontrar la información.")
    print("\n")

def convertirMonedas():
    try:
        fuente = input("Ingrese el código de moneda fuente: ").upper()
        blanco = input("Ingrese el codigo de moneda de destino: ").upper()
        cant = float(input("Ingrese la cantidad a convertir: "))
        url = f'https://api.currencyfreaks.com/v2.0/convert/latest?apikey={apikey}&from={fuente}&to={blanco}&amount={cant}'
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            datos = respuesta.json()
            convertido = datos.get('convertedAmount')
            if convertido:
                print(f'{cant} {fuente} es igual a {convertido} {blanco}')
            else:
                print('Error: No se encontraron datos de conversión en la respuesta del API')
        else:
            print(f'Error: Codigo de estado: {respuesta.status_code}')
    except ValueError as e:
        print("Error: ", e)
    texto_json = json.dumps(datos, indent=2)
    with open("conversion.txt", "a") as archivo:
        archivo.write("\n")
        archivo.write(texto_json)
        archivo.write("\n")
    print("\n")

def consultarTasas():
    open_in_idle("GCMStats.py")

def salir():
    print("Adios!")
    return False

def main():
    opciones ={
        1: consultarMonedas,
        2: convertirMonedas,
        3: consultarTasas,
        4: salir
    }
    menu()
    banderaMenu = True
    while banderaMenu:
        try:
            op = int(input("Elige el número de la opción que desea realizar: "))
            elegida = opciones.get(op)
            if elegida:
                resultado = elegida()
                if resultado is False:
                    banderaMenu = False
            else:
                print("Error: Opción inválida.")
        except ValueError:
            print("Error: Debes ingresar un número.")
main()
