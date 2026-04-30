numero = int(input("Ingrese un numero entero positivo: "))

if numero % 2 == 0 and numero > 10:
    print("Numero par y mayor que 10")
elif numero % 2 == 0 and numero <= 10:
    print("Numero par y menor o igual que 10")
elif numero % 2 != 0:
    print("Es impar")