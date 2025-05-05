# ordenador.py

class OrdenadorPila:
    @staticmethod
    def ordena(pila):
        """
        Recibe una pila (lista) de enteros y la ordena de mayor (fondo) a menor (cima),
        usando solo operaciones de pila: pop() y append().
        """
        pila_aux = []

        while pila:
            # Sacamos el tope de la pila original
            temp = pila.pop()

            # Mientras la pila auxiliar tenga elementos menores, los devolvemos a la pila original
            while pila_aux and pila_aux[-1] < temp:
                pila.append(pila_aux.pop())

            # Colocamos temp en su lugar correcto en la pila auxiliar
            pila_aux.append(temp)

        # pila_aux tiene los elementos de mayor (fondo) a menor (top),
        # hacemos una copia para mantener el orden
        resultado = pila_aux.copy()

        return resultado