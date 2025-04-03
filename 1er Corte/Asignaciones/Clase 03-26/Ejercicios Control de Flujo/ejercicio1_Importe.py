"""Desarrolla un programa que calcule el importe a pagar
por un vehiculo al circular por una autopista. El vehiculo
puede ser una bicicleta, una moto, un carro o un camion.
Para definir el conjunto de vehiculos debes utilizar una
estructura adecuada. El importe se calculara segun los
siguientes datos:

A. Importe fijo 100 cordobas para bicicleta
B. Motos y carros pagaran 30 cordobas por km
C. Los camiones pagaran 30 cordobas por km + 25 cordobas por tonelada
"""
def moto_carro_importe(km):
    return 30 * km

def camion_importe(km, ton):
    return (30 * km) + (25 * ton)

def calcular_importe(vehiculo):
    vehiculo = vehiculo.lower().strip()

    if vehiculo == "bicicleta":
        return 100  # Importe fijo para bicicleta
    elif vehiculo in ["moto", "carro"]:
        km = int(input("¿Cuántos km recorrió con su vehículo ligero? "))
        return moto_carro_importe(km)
    elif vehiculo == "camion":
        km = int(input("¿Cuántos km recorrió con su camión? "))
        ton = int(input("¿Cuántas toneladas pesa su camión? "))
        return camion_importe(km, ton)
    else:
        return "Tipo de vehículo no válido."

while True:
    vehiculo_elegido = input("¿Qué vehículo tienes? (bicicleta, moto, carro, camión): ").strip()
    importe = calcular_importe(vehiculo_elegido)

    print(f"El importe a pagar es: {importe} córdobas")

    otra_gestion = input("\n¿Desea realizar otra gestión? (si/no): ").strip().lower()
    if otra_gestion != 'si':
        break  # Sale del bucle si el usuario no quiere continuar