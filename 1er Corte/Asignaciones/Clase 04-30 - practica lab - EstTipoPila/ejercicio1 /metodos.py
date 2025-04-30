#metodo que separa los números pares e impares en una pila
def separar_par_impar(pila):
    # listas auxiliares para pares e impares
    pares = []
    impares = []

    # desapilamos y clasificamos cada número
    while not pila.esta_vacia():
        numero = pila.desapilar()
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)

    # reconstruimos la pila original con pares al fondo y luego impares
    for numero in reversed(impares):
        pila.apilar(numero)
    for numero in reversed(pares):
        pila.apilar(numero)

    return pila