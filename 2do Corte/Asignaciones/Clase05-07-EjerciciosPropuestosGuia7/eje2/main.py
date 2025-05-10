from estrucBasePiladobleEnlazada import Node as Pan, Stack as BandejaDePanes
from estrucMenu import Menu, MenuOption

bandeja = BandejaDePanes()

def agregar_pan():
    tipo = input("Ingrese el tipo de pan recién horneado: ")
    nuevo_pan = Pan(tipo)
    bandeja.push(nuevo_pan)
    print(f"Pan '{tipo}' agregado a la bandeja.")

def vender_pan():
    try:
        vendido = bandeja.pop()
        print(f"Se vendió un pan de tipo: '{vendido.data}'")
    except IndexError:
        print("No hay panes para vender.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def ver_pan_listo():
    try:
        pan_listo = bandeja.peek()
        if pan_listo is None:
            print("No hay panes listos para vender.")
        else:
            print(f"El pan listo para vender es: '{pan_listo.data}'")
    except IndexError:
        print("No hay panes listos para vender.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_panes():
    actual = bandeja.tail
    if not actual:
        print("No hay panes en la bandeja.")
        return
    print("Panes en la bandeja (del más antiguo al más reciente):")
    while actual:
        print(f"- {actual.data}")
        actual = actual.prev

menu = Menu("Gestión de Bandeja de Panes", [
    MenuOption("1", "Agregar pan horneado", agregar_pan),
    MenuOption("2", "Vender pan", vender_pan),
    MenuOption("3", "Ver pan listo para vender", ver_pan_listo),
    MenuOption("4", "Mostrar todos los panes en bandeja", mostrar_panes),
])

if __name__ == "__main__":
    menu.show()