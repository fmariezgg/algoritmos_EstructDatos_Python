class Perro:
    def __init__ (self,nombre,raza,altura):
        self.nombre = nombre
        self.raza = raza
        self.altura = altura

    def comer(self):
        return "El perro esta comiendo..."

    def dormir(self):
        return "El perro esta durmiendo..."

    def ladrar(self):
        return "El pero esta ladrando..."

    def lamer(self):
        return  "El perro se esta lamiendo..."

firu = Perro('Firulai', 'Pastor Aleman', 0.6)
Sisi = Perro('Sisi', "Chihuahua", '0.3')

print(firu.nombre)
print(firu.raza)
print(firu.altura)
print(firu.comer())
print(firu.dormir())
print(firu.lamer())


