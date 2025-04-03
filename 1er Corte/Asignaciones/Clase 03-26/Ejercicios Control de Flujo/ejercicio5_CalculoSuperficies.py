import math

def calcular_area():
    while True:
        print("""
        *.*.*.*.*.*.*.*.*.*.*.*.*.*.*
             CÁLCULO DE SUPERFICIES 
        *.*.*.*.*.*.*.*.*.*.*.*.*.*.*
        1. Cuadrado      -> lado * lado
        2. Círculo       -> pi * radio * radio
        3. Rectángulo    -> base * altura
        4. Trapecio      -> (base1 + base2) * altura / 2
        5. Triángulo     -> (base * altura) / 2
         *.*.*.*.*.*.*.*.*.*.*.*.*.*.*
        """)

        opcion = int(input("Seleccione una opción (1-5) o 'q' para salir: "))

        match opcion:
            case 1: 
                lado = float(input("Ingrese el lado del cuadrado: "))
                area = lado * lado
            case 2:
                radio = float(input("Ingrese el radio del círculo: "))
                area = math.pi * radio * radio
            case 3:
                base = float(input("Ingrese la base del rectángulo: "))
                altura = float(input("Ingrese la altura del rectángulo: "))
                area = base * altura
            case 4:
                base1 = float(input("Ingrese la base menor del trapecio: "))
                base2 = float(input("Ingrese la base mayor del trapecio: "))
                altura = float(input("Ingrese la altura del trapecio: "))
                area = (base1 + base2) * altura / 2
            case 5:
                base = float(input("Ingrese la base del triángulo: "))
                altura = float(input("Ingrese la altura del triángulo: "))
                area = (base * altura) / 2
            case 'q':
                print("saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente nuevamente.")
                continue

        print(f"El área calculada es: {area:.2f}\n")


calcular_area()
