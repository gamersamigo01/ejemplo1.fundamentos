precio = int(input("Ingrese el precio del producto: "))

if precio != 0:
    socio = input("Ingrese si usted es socio(s/n): ").lower().strip()
    if precio > 50_000 and socio == "s":
        descuento = 0.20
    elif precio > 50_000 and socio == "n":
        descuento = 0.10
    elif precio <= 50_000 and socio == "s":
        descuento = 0.05
    else:
        descuento = 0

final = precio * (1-descuento)

print(f"Precio: {precio}")
print(f"¿Eres socio? (s/n): {socio}")
print(f"Precio con descuento: {final}")