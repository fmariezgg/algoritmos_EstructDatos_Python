"""
Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo
un descuento del 15% por la compra de más de 3 docenas y 10% en caso contrario.
Además, por la compra de más de 3 docenas se obsequia una unidad del producto
por cada docena en exceso sobre 3. Diseñe un programa que determine el monto de
la compra, el monto del descuento, el monto a pagar y el número de unidades de obsequio
por la compra de cierta cantidad de docenas del producto.

"""
while True:
    try:
        precio_por_docena = float(input("Ingrese el precio por docena del producto: "))
        cantidad_docenas = int(input("Ingrese la cantidad de docenas que desea comprar: "))

        monto_compra = precio_por_docena * cantidad_docenas

        if cantidad_docenas > 3:
            descuento = monto_compra * 0.15  # 15% de descuento
            obsequios = cantidad_docenas - 3  # Una unidad por cada docena extra sobre 3
        else:
            descuento = monto_compra * 0.10  # 10% de descuento
            obsequios = 0  # No hay obsequios

        monto_a_pagar = monto_compra - descuento

        print(f"\nResumen de la compra:")
        print(f"Monto de la compra: {monto_compra:.2f} córdobas")
        print(f"Monto del descuento: {descuento:.2f} córdobas")
        print(f"Monto a pagar: {monto_a_pagar:.2f} córdobas")
        print(f"Unidades de obsequio: {obsequios}")

        otra_compra = input("\n¿Desea realizar otra compra? (si/no): ").strip().lower()
        if otra_compra != 'si':
            break
    except ValueError:
        print("Error: Por favor ingrese valores numéricos válidos.")
