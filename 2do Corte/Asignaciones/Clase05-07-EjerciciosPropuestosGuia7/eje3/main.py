from estrucBasePiladobleEnlazada import Node as Donante, Stack as PilaDeDonantes
from estrucMenu import Menu, MenuOption

pila = PilaDeDonantes()

def registrar_donante():
    nombre = input("Ingrese el nombre del donante: ")
    nuevo_donante = Donante(nombre)
    pila.push(nuevo_donante)
    print(f"Donante '{nombre}' registrado en el sistema.")

def revertir_registro():
    try:
        cancelado = pila.pop()
        print(f"Registro revertido: '{cancelado.data}' ha sido eliminado.")
    except IndexError:
        print("No hay registros para revertir.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_donante_actual():
    try:
        actual = pila.peek()
        if actual is None:
            print("No hay donantes en proceso.")
        else:
            print(f"Donante actual en proceso: '{actual.data}'")
    except IndexError:
        print("No hay donantes en proceso.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def listar_donantes():
    actual = pila.tail
    if not actual:
        print("No hay donantes registrados.")
        return
    print("Lista de donantes (del más antiguo al más reciente):")
    while actual:
        print(f"- {actual.data}")
        actual = actual.prev

menu = Menu("Registro de Donantes - Hospital Estelí", [
    MenuOption("1", "Registrar nuevo donante", registrar_donante),
    MenuOption("2", "Revertir último registro", revertir_registro),
    MenuOption("3", "Mostrar donante actual en proceso", mostrar_donante_actual),
    MenuOption("4", "Listar todos los donantes", listar_donantes),
])

if __name__ == "__main__":
    menu.show()