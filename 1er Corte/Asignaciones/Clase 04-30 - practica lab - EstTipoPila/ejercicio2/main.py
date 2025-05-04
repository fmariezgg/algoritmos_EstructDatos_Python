# main.py
'''
proyecto_ordenador_pila/
├── ordenador.py      # Clase con el metodo 'ordena'
├── main.py           # Interfaz con menú para ingresar y ordenar pilas
'''

# main.py

from ordenador import OrdenadorPila

def mostrar_menu():
    print("\n--- ORDENAR PILA ---")
    print("1. Ingresar pila de enteros")
    print("2. Salir")

def ingresar_pila():
    pila = []
    print("Ingrese números enteros uno por uno.")
    print("Escriba 'fin' para terminar la entrada.")
    while True:
        entrada = input("Número: ")
        if entrada.lower() == "fin":
            break
        if entrada.isdigit() or (entrada.startswith("-") and entrada[1:].isdigit()):
            pila.append(int(entrada))
        else:
            print("Entrada no válida. Ingrese un número entero o 'fin'.")
    return pila

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            pila_usuario = ingresar_pila()
            if not pila_usuario:
                print("La pila está vacía.")
                continue

            resultado = OrdenadorPila.ordena(pila_usuario.copy())
            print("\nPila original:", pila_usuario)
            print("Pila ordenada (mayor al fondo, menor arriba):", resultado)

        elif opcion == "2":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()