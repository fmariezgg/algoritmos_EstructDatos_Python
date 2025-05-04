# ordenador.py

class OrdenadorPila:
    @staticmethod
    def ordena(pila):
        """
        Recibe una pila de enteros (lista) y la devuelve ordenada de mayor a menor.
        El número mayor queda en el fondo (inicio de la lista) y el menor en la cima (último).
        """
        # Ordenamos la lista en orden descendente
        pila_ordenada = sorted(pila, reverse=True)
        return pila_ordenada