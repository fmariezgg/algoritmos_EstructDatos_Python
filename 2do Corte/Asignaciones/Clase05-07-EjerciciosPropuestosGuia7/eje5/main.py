from estrucBasePiladobleEnlazada import Node as Saco, Stack as PilaDeSacos
from estrucMenu import Menu, MenuOption

camion = PilaDeSacos()

def cargar_saco():
    tipo = input("Ingrese el tipo de producto del saco (ej. frijoles, arroz): ")
    nuevo_saco = Saco(tipo)
    camion.push(nuevo_saco)
    print(f"Saco de '{tipo}' cargado en el camión.")

def descargar_saco():
    try:
        descargado = camion.pop()
        print(f"Saco de '{descargado.data}' ha sido descargado.")
    except IndexError:
        print("No hay sacos para descargar.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def ver_saco_superior():
    try:
        saco = camion.peek()
        if saco is None:
            print("No hay sacos en el camión.")
        else:
            print(f"Saco en la cima: '{saco.data}'")
    except IndexError:
        print("No hay sacos en el camión.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def listar_sacos():
    actual = camion.tail
    if not actual:
        print("No hay sacos cargados.")
        return
    print("Sacos cargados (del más antiguo al más reciente):")
    while actual:
        print(f"- {actual.data}")
        actual = actual.prev

menu = Menu("Gestión de Sacos - Mercado de Chinandega", [
    MenuOption("1", "Cargar nuevo saco", cargar_saco),
    MenuOption("2", "Descargar saco superior", descargar_saco),
    MenuOption("3", "Ver saco en la cima", ver_saco_superior),
    MenuOption("4", "Listar todos los sacos cargados", listar_sacos),
])

if __name__ == "__main__":
    import os
    # Limpiar pantalla antes de iniciar el menú
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    menu.show()