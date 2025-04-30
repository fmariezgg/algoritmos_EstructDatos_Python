# clase que define la estructura de una pila
class Pila:
    def __init__(self):
        # lista interna que representa los elementos de la pila
        self.elementos = []

    def apilar(self, elemento):
        # agrega un elemento al tope de la pila
        self.elementos.append(elemento)

    def desapilar(self):
        # elimina y retorna el elemento del tope de la pila si no está vacía
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        # retorna true si la pila no tiene elementos
        return len(self.elementos) == 0

    def ver_elementos(self):
        # retorna una copia de los elementos actuales en la pila
        return self.elementos.copy()

    def vaciar(self):
        # elimina todos los elementos de la pila
        self.elementos.clear()