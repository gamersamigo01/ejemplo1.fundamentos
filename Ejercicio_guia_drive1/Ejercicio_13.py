num = int(input("Ingrese un numero entero positivo: "))
guardado = 1
if num < 0:
    print("El numero no puede ser negativo")
elif num == 0:
    print("El factorial de 0 es 1")
else:
    for i in range(1,num+1):
        guardado = guardado * i
    print(f"El factorial de {num} es: {guardado}")
