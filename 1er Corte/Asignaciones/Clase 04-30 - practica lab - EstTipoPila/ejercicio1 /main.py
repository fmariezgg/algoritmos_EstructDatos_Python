from clases import Pila
from metodos import separar_par_impar

# creamos una instancia de pila
mi_pila = Pila()

# valores de entrada
entrada = [2, 3, 6, 8, 11, 13, 18, 21]
for numero in entrada:
    mi_pila.apilar(numero)

# aplicamos el metodo para separar pares e impares
separar_par_impar(mi_pila)

# mostramos la pila resultante
print("pila separada:", mi_pila.ver_elementos())