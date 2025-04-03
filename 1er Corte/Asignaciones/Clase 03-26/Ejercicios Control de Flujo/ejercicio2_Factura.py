"""
Escribir un programa que permita emitir la FACTURA correspondiente, a una compra de un artículo determinado,
 del que se adquieren una o varias unidades. El IVA a aplicar es de 15% y si el Sub Total
 (precio de venta por cantidad), es mayor de 1000, se aplicará un descuento del 12%.
"""
while True:

    print("\n------ FACTURA DE COMPRA --------")

 #input
    nombre_articulo = input("Ingrese el nombre del artículo: ")
    precio_unitario = float(input("Ingrese el precio unitario del artículo: ""C$"))
    cantidad = int(input("Ingrese la cantidad de unidades compradas: "))

    subtotal = precio_unitario * cantidad

#aplicar descuento del 12% si el subtotal es mayor a 1000
    descuento = 0
    if subtotal > 1000:
        descuento = subtotal * 0.12

    subtotal_con_descuento = subtotal - descuento
    iva = subtotal_con_descuento * 0.15

    total = subtotal_con_descuento + iva

    #Mostrar factura
    print("\n------ FACTURA ------")
    print(f"Artículo: {nombre_articulo}")
    print(f"Precio unitario: C${precio_unitario:.2f} ")
    print(f"Cantidad: {cantidad}")
    print(f"Subtotal: C${subtotal:.2f} ")
    print(f"Descuento aplicado: C${descuento:.2f} ")
    print(f"IVA (15%): C${iva:.2f} ")
    print(f"TOTAL A PAGAR: C${total:.2f} ")

    #En caso si desea realizar otra compra
    otra_compra = input("\n¿Desea realizar otra compra? (si/no): ").strip().lower()
    if otra_compra != 'si':
        print("Gracias por su compra. ¡Vuelva pronto!")
        break