'''
Andres Castillo
Fatima Zogaib


Problema#3
Una clínica recibe pacientes en orden de llegada. Cada paciente debe ser ingresado al sistema
con los siguientes datos: nombre completo, edad, síntoma principal y prioridad (de 1 a 5). El
sistema debe permitir insertar nuevos pacientes, recorrer la lista para mostrar el orden de
atención, y eliminar a un paciente una vez atendido.
'''

import time
#para hacer pausas y dar tiempo al usuario a leer.
import os
#limpiar la pantalla

def limpiar_pantalla():
    time.sleep(2)  #espera 2 segundos antes de limpiar la pantalla
    os.system('cls' if os.name == 'nt' else 'clear')

#clase que representa a un paciente en la lista
class Paciente:
    def __init__(self, nombre, edad, sintoma, prioridad):
        self.nombre = nombre
        self.edad = edad
        self.sintoma = sintoma
        self.prioridad = prioridad
        self.siguiente = None  #referencia al siguiente paciente (es una lista enlazada)

#clase que maneja y guarda la lista enlazada de pacientes
class ListaPacientes:
    def __init__(self):
        self.inicio = None  #la lista inicia vacía

    #metodo para insertar un paciente en la lista respetando el orden de prioridad
    def insertar_paciente(self, nombre, edad, sintoma, prioridad):
        nuevo = Paciente(nombre, edad, sintoma, prioridad)
        #si la lista está vacía o el nuevo paciente tiene mayor prioridad
        if self.inicio is None or prioridad < self.inicio.prioridad:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
            print(f"\033[93m{nombre} ha sido ingresado con alta prioridad.\033[0m")
        else:
            #buscar la posición adecuada según la prioridad
            actual = self.inicio
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            print(f"\033[93m{nombre} ha sido ingresado en la lista de espera.\033[0m")
        time.sleep(2)  #simula una pausa para una transición suave

    #metodo para mostrar la lista de pacientes en orden de atención
    def mostrar_pacientes(self):
        if self.inicio is None:
            print("\033[91mNo hay pacientes en espera.\033[0m")
            return
        actual = self.inicio
        print("\nLista de Pacientes en Orden de Atención:")
        while actual:
            print(f"Nombre: {actual.nombre}, Edad: {actual.edad}, Síntoma: {actual.sintoma}, Prioridad: {actual.prioridad}")
            actual = actual.siguiente
            time.sleep(2)  #pausa para simular animación

    #metodo para atender (eliminar) al primer paciente de la lista
    def atender_paciente(self):
        if self.inicio is None:
            print("\033[91mNo hay pacientes para atender.\033[0m")
            return
        atendido = self.inicio
        self.inicio = self.inicio.siguiente  #el siguiente paciente pasa a ser el primero
        print(f"\033[93m{atendido.nombre} ha sido atendido.\033[0m")
        time.sleep(2)  #simula una transición después de atender

#funcion que muestra el menú principal del sistema
def menu():
    lista = ListaPacientes()  #crea una lista vacía de pacientes
    # bucle principal del menú
    while True:
        print("\n\033[94m----- Clínica de Atención Médica -----\033[0m")
        print("\033[92m1. Ingresar nuevo paciente\033[0m")
        print("\033[92m2. Mostrar pacientes en espera\033[0m")
        print("\033[92m3. Atender al siguiente paciente\033[0m")
        print("\033[92m4. Salir\033[0m")
        opcion = input("Seleccione una opción: ")

        # opción para ingresar un nuevo paciente
        if opcion == '1':
            # solicitar nombre del paciente
            while True:
                nombre = input("Nombre completo: ").strip()
                if nombre:
                    break
                else:
                    print("\033[91mEl nombre no puede estar vacío.\033[0m")
                    time.sleep(2)

            # solicitar edad del paciente con validación
            while True:
                try:
                    edad = int(input("Edad: "))
                    break
                except ValueError:
                    print("\033[91mEdad inválida. Debe ingresar un número entero.\033[0m")
                    time.sleep(2)

            # solicitar síntoma del paciente
            while True:
                sintoma = input("Síntoma principal: ").strip()
                if sintoma:
                    break
                else:
                    print("\033[91mEl síntoma no puede estar vacío.\033[0m")
                    time.sleep(2)

            # solicitar prioridad del paciente con validación
            while True:
                try:
                    prioridad = int(input("Prioridad (1 más alto - 5 más bajo): "))
                    if 1 <= prioridad <= 5:
                        break
                    else:
                        print("\033[91mPrioridad inválida. Debe ser entre 1 y 5.\033[0m")
                        time.sleep(2)
                except ValueError:
                    print("\033[91mPrioridad inválida. Debe ingresar un número entero.\033[0m")
                    time.sleep(2)

            lista.insertar_paciente(nombre, edad, sintoma, prioridad)
            limpiar_pantalla()

        # opción para mostrar la lista de pacientes
        elif opcion == '2':
            lista.mostrar_pacientes()
            limpiar_pantalla()

        # opción para atender al siguiente paciente
        elif opcion == '3':
            lista.atender_paciente()
            limpiar_pantalla()

        # opción para salir del sistema
        elif opcion == '4':
            print("\033[93mVuelva pronto :)\033[0m")
            break

        # manejo de opción inválida
        else:
            print("\033[91mOpción no válida. Intente de nuevo.\033[0m")
            time.sleep(2)
            limpiar_pantalla()

#punto de entrada del programa
if __name__ == "__main__":
    menu()