# Clase para crear nodos
class Nodo():

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

# Función para agregar nodos al final de la lista
def agregar_al_final(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    if nodo_inicial == None:
        nodo_inicial = nuevo_nodo
        return nodo_inicial
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    temporal.siguiente = nuevo_nodo
    return nodo_inicial

# Función para agregar nodos al inicio de la lista
def agregar_al_inicio(nodo_inicial, dato):
    nuevo_nodo = Nodo(dato)
    nuevo_nodo.siguiente = nodo_inicial
    return nuevo_nodo

# Función para imprimir la lista
def imprimir_lista(nodo):
    while nodo != None:
        print(f"Tenemos {nodo.dato}")
        nodo = nodo.siguiente

# Función para obtener el nodo inicial
def obtener_cabeza(nodo_inicial):
    return nodo_inicial

# Función para obtener el final de la lista
def obtener_cola(nodo_inicial):
    temporal = nodo_inicial
    while temporal.siguiente:
        temporal = temporal.siguiente
    return temporal

# Función para saber si un nodo existe en la lista
def existe(nodo, busqueda):
    while nodo != None:
        if nodo.dato == busqueda:
            return True
        nodo = nodo.siguiente
    return False

# Función para eliminar nodo
def eliminar(nodo, busqueda):
    if nodo == None:
        return nodo
    if nodo.dato == busqueda:
        return nodo.siguiente
    temporal = nodo
    while temporal.siguiente != None:
        if temporal.siguiente.dato == busqueda:
            if temporal.siguiente.siguiente != None:
                temporal.siguiente = temporal.siguiente.siguiente
            else:
                temporal.siguiente = None
            return nodo
        temporal = temporal.siguiente
    return nodo

def main():
    lista = None
    lista = agregar_al_final(lista, "Raúl")
    lista = agregar_al_final(lista, "Marcos")
    lista = agregar_al_inicio(lista, "Enlace")
    print("Antes de eliminar: ")
    imprimir_lista(lista) # Enlace, Raúl, Marcos
    lista = eliminar(lista, "Enlace")
    print("Después de eliminar: ")
    imprimir_lista(lista) # Raúl, Marcos
    print(existe(lista, "Enlace")) # False
    print(existe(lista, "Raúl"))   # True
    # obtener_cabeza nos regresa el nodo, pero accedemos al dato para imprimirlo
    print(obtener_cabeza(lista).dato) # Raúl
    print(obtener_cola(lista).dato)   # Marcos

main()