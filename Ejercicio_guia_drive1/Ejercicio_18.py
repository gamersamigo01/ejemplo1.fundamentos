texto = input("Ingrese un texto: ")

texto_limpio = texto.lower().strip()
texto_inverso = texto_limpio[::-1]
texto_inverso = " ".join(texto_inverso.split())
print(texto_inverso)
if texto_limpio == texto_inverso:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")