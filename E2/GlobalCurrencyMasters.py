import requests
import json
apikey = '7a86521fff0242e4b35bf70ee3696f80'

def menu():
    print("""###Global###Currency###Masters###
###           ###                ###              ###
###           ###                ###              ###
###           ###                ###              ###
###           ###                ###              ###
print("1. Consultar tipos de monedas")
print("2. Convertir fuente a blanco")
print("3. Salir")""")

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
    with open("conversion.txt", "w") as archivo:
        archivo.write(texto_json)
    print("\n")

def main():
    menu()
    banderaMenu = True
    while banderaMenu:
        op = int(input("Elige el número de la opción que desea realizar: "))
        if op == 1:
            consultarMonedas()
            continue
        elif op == 2:
            convertirMonedas()
            continue
        elif op == 3:
            print("Adios!")
            banderaMenu = False
            break
        else:
            print("Error: Opción inválida.")

main()
