from estrucBasePiladobleEnlazada import Node as Tarea, Stack as PilaDeTareas
from estrucMenu import Menu, MenuOption

pila = PilaDeTareas()

def agregar_tarea():
    estudiante = input("Ingrese el nombre del estudiante o título de la tarea: ")
    nueva_tarea = Tarea(estudiante)
    pila.push(nueva_tarea)
    print(f"Tarea de '{estudiante}' agregada a la pila para revisión.")

def revisar_tarea():
    try:
        tarea = pila.pop()
        print(f"Se ha revisado la tarea de: '{tarea.data}'")
    except IndexError:
        print("No hay tareas para revisar.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def mostrar_siguiente_tarea():
    try:
        siguiente = pila.peek()
        if siguiente is None:
            print("No hay tareas pendientes.")
        else:
            print(f"Próxima tarea a revisar: '{siguiente.data}'")
    except IndexError:
        print("No hay tareas pendientes.")
    except Exception as e:
        print(f"Error inesperado: {e}")

def listar_tareas():
    actual = pila.tail
    if not actual:
        print("No hay tareas registradas.")
        return
    print("Tareas pendientes (de la más antigua a la más reciente):")
    while actual:
        print(f"- {actual.data}")
        actual = actual.prev

menu = Menu("Sistema de Revisión de Tareas - Docente de Informática", [
    MenuOption("1", "Agregar tarea impresa", agregar_tarea),
    MenuOption("2", "Revisar la tarea superior", revisar_tarea),
    MenuOption("3", "Mostrar próxima tarea a revisar", mostrar_siguiente_tarea),
    MenuOption("4", "Listar todas las tareas pendientes", listar_tareas),
])

if __name__ == "__main__":
    menu.show()