#Calcular el total a pagar en una tienda con su impuesto y descuento
precio_bruto = float(input("Ingrese el precio total de la compra: "))
iva = precio_bruto * 0.15
descuento = precio_bruto * 0.25
total = precio_bruto + iva - descuento
print(f"El precio total a pagar por su compra es: {total}")