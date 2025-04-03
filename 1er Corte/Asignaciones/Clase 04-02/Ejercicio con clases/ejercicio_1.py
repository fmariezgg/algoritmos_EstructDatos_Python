class Estudiante:
    def __init__(self,nombre,nota):
        self.nombre = nombre
        self.nota = nota

    def datos_alumno(self):
       print(f"Nombre alumno: {self.nombre}")
       print(f"Nota alumno: {self.nota}")

    def calificacion(self):
        if int(self.nota) >= 70:
            return "Aprobado"
        else:
            return "Reprobado"



estudiante = Estudiante("Marie",80)
estudiante.datos_alumno()
print(estudiante.calificacion())
