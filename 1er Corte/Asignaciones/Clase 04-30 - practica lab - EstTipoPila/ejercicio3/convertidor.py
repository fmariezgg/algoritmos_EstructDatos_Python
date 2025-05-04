# convertidor.py

class ConvertidorBinario:
    @staticmethod
    def Convbinario(numero):
        """
        Convierte un número entero a binario usando una pila.
        Retorna el binario como una cadena dentro de una lista: [binario]
        """
        if numero == 0:
            return ["0"]

        pila = []

        # División sucesiva entre 2, guardando los residuos
        while numero > 0:
            residuo = numero % 2
            pila.append(str(residuo))
            numero //= 2

        binario = ""
        while pila:
            binario += pila.pop()

        return [binario]