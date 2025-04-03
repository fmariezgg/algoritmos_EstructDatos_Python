#Leer el precio de un producto y calcule el IVA
precio = float(input("Ingrese el precio del producto: "))
iva = precio * 0.15
total = precio + iva
print(f"El IVA es: {iva}")
print(f"El precio total del producto es: {total}")
