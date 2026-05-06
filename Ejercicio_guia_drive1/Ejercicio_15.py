import random
import string
random_num = random.randint(1, 100)
intentos = 0
while True:
    num = int(input("Adivine un numero del 1 al 100: "))
    intenos += 1
    if num > random_num:
        print("Su numero es mayor que el numero correcto: ")
    elif num < random_num:
        print("Su numero es menor que el numero correcto: ")
    else:
        print("¡Correcto!")
        print(f"Intentos: {intenos}")
        break