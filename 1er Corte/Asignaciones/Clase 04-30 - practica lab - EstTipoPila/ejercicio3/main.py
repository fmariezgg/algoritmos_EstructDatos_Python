'''
proyecto_convertidor_binario/
├── convertidor.py    # Clase con el metodo Convbinario
├── main.py           # Interfaz con menú para ingresar un entero y ver el binario
'''

# main.py

from convertidor import ConvertidorBinario

def mostrar_menu():
    print("\n--- CONVERTIR ENTERO A BINARIO ---")
    print("1. Ingresar número entero")
    print("2. Salir")

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            entrada = input("Ingrese un número entero: ")
            if entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit()):
                numero = int(entrada)
                if numero < 0:
                    print("El número debe ser positivo.")
                    continue
                resultado = ConvertidorBinario.Convbinario(numero)
                print(f"Representación binaria: {resultado}")
            else:
                print("Entrada inválida. Intente nuevamente.")

        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()