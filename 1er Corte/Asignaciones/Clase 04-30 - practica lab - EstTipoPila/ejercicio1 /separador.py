# separador.py

class SeparadorPila:
    @staticmethod
    def separar_par_impar(pila):
        """
        Metodo que recibe una pila (lista) de enteros y devuelve una nueva pila
        con los números pares en la parte inferior y los impares en la parte superior.
        """
        pila_pares = []
        pila_impares = []

        while pila:
            numero = pila.pop()
            if numero % 2 == 0:
                pila_pares.append(numero)
            else:
                pila_impares.append(numero)

        nueva_pila = []

        while pila_pares:
            nueva_pila.append(pila_pares.pop())

        while pila_impares:
            nueva_pila.append(pila_impares.pop())

        return nueva_pila