numero = int(input("ingrese un numero: "))

if numero > 0:
    elevado = numero ** 2
    print(f"Su numero positivo elevado a 2 es: {elevado}")
elif numero == 0:
    print("Su numero es 0 por lo tanto su numero elevado es: 0")
else:
    print("El numero es negativo, no se calcula el cuadrado")