nombre_producto = input("Ingrese el nombre del producto: ")
precio = int(input("Ingrese el precio del producto: "))

if precio > 1000:
    precio = precio - (precio * 0.15)
elif precio <= 1000:
    precio = precio - (precio * 0.05)

print(f"Su producto {nombre_producto} tiene un valor de: {precio:.2f} con descuento")# EL :.2f sirve para aproximar a la centesima