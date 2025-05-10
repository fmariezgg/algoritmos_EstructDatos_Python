from estrucBasePiladobleEnlazada import Node as Documento, Stack as DocumentosARevisar
from estrucMenu import Menu, MenuOption

documentos = DocumentosARevisar()

def agregar_documento():
    titulo = input("Ingrese el título del nuevo documento: ")
    nuevo = Documento(titulo)
    documentos.push(nuevo)
    print(f"Documento '{titulo}' agregado a la pila.")

def quitar_documento():
    eliminado = documentos.pop()
    if eliminado:
        print(f"Documento '{eliminado.data}' fue revisado y retirado.")
    else:
        print("No hay documentos para revisar.")

def ver_ultimo_documento():
    try:
        actual = documentos.peek()
        if actual is None:
            print("No hay documentos en la pila.")
        else:
            print(f"El documento en la cima es: '{actual.data}'")
    except IndexError:  # Específicamente para manejar la excepción cuando la pila está vacía
        print("No hay documentos en la pila.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_documentos():
    actual = documentos.tail
    if not actual:
        print("No hay documentos pendientes.")
        return
    print("Documentos pendientes (de encima para abajo):")
    while actual:
        print(f"- {actual.data}")
        actual = actual.prev

menu = Menu("Gestión de Documentos a Revisar", [
    MenuOption("1", "Agregar documento", agregar_documento),
    MenuOption("2", "Quitar documento revisado", quitar_documento),
    MenuOption("3", "Ver documento en la cima", ver_ultimo_documento),
    MenuOption("4", "Mostrar todos los documentos pendientes", mostrar_documentos),
])

if __name__ == "__main__":
    menu.show()