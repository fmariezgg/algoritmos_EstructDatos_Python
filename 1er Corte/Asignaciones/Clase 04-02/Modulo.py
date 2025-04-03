class Alumno:
    def __init__(self,nombre,edad):#para definir constructor, se usan dos guiones bajos
        self.edad=edad #propiedad, valor
        self.nombre=nombre

    def saludar(self):
        print(f"Hola, {self.nombre} tu edad es {self.edad}")