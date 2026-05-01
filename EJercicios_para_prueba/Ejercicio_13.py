cadena = input("Ingrese un texto: ")

if len(cadena) > 10:
    cadena = cadena.upper()

elif len(cadena) <= 10:
    cadena = cadena.lower()

print(f"Texto transformado: {cadena}")
