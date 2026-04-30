numero = int(input("ingrese un numero entero: "))
actualizado = numero + 10

if actualizado % 3 == 0 and actualizado % 5 == 0:
    print("Su numero mas, 10 es multiplo de 3 y 5")
else:
    print("Su numero mas 10, no es multiplo de 3 y 5")