def obtener_impares(n):
    """Genera una lista de números impares hasta n."""
    return [i for i in range(1, n + 1, 2)]

def suma_impares(numeros):
    """Calcula la suma de los números impares en la lista."""
    return sum(numeros)


def producto_impares(numeros):
    """Calcula el producto de los números impares en la lista."""
    producto = 1
    for num in numeros:
        producto *= num
    return producto


def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Introducir un valor entero impar entre 1 y 19")
        print("2. Calcular la suma de la serie 1 + 3 + 5 + ... + n")
        print("3. Calcular el producto de la serie 1 * 3 * 5 * ... * n")
        print("4. Salir del programa")

        opcion = input("Seleccione una opción (1-4): ")

        if opcion == '1':
            try:
                n = int(input("Ingrese un número impar entre 1 y 19: "))
                if n < 1 or n > 19 or n % 2 == 0:
                    print("⚠️ Debe ser un número impar entre 1 y 19.")
                else:
                    print(f"Número guardado: {n}")
            except ValueError:
                print("⚠️ Entrada no válida. Debe ser un número entero.")

        elif opcion == '2':
            if 'n' in locals():
                impares = obtener_impares(n)
                print(f"Suma de la serie: {suma_impares(impares)}")
            else:
                print("⚠️ Primero debe ingresar un número válido en la opción 1.")

        elif opcion == '3':
            if 'n' in locals():
                impares = obtener_impares(n)
                print(f"Producto de la serie: {producto_impares(impares)}")
            else:
                print("⚠️ Primero debe ingresar un número válido en la opción 1.")

        elif opcion == '4':
            print("Saliendo del programa... 👋")
            break

        else:
            print("⚠️ Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
