frase = input("Ingrese una frase: ").lower()
palabras = "aeiou"
suma = 0
for i in frase:
    if i in palabras:
        suma += 1
print(f"tiene {suma} vocales")

