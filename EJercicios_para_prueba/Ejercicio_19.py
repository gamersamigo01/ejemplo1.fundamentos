numero = int(input("Ingrese un numero: "))

if numero < 0:
    numero = -numero 

print(f"numero absoluto: {numero}")
division = numero // 3

print(f"El numero 3 cabe {division} veces en su numero {numero}")