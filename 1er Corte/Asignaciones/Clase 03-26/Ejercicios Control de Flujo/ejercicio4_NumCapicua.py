def mostrar_menu():
    """
    Muestra el menú de opciones para verificar un número capicúa.
    """
    print("""
    =============================
    Verificación de número capicúa
    =============================
    1. Ingresar un número
    2. Salir
    """)


def es_capicua(numero: str) -> str:
    """
    Verifica si un número de tres cifras es capicúa.
    :param numero: Número ingresado como cadena.
    :return: Mensaje indicando si es capicúa o no.
    """
    if not numero.isdigit() or len(numero) != 3:
        return " Error: Debe insertar un número de 3 cifras."

    return "El número es capicúa." if numero[0] == numero[2] else "El número no es capicúa."


def main():
    """
    Función principal que ejecuta el programa.
    """
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1/2): ").strip()

        if opcion == '1':
            numero = input("Ingrese un número de 3 cifras: ").strip()
            print(es_capicua(numero))
        elif opcion == '2':
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()
