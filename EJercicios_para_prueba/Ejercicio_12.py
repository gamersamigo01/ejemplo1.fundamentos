num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

num1 = num1 + num2
num2 -= 3
print(f"Numero 1 actualizado: {num1}")
print(f"numero 2 actualizado: {num2}")

if num1 > num2:
    print("El primer numero es mayor al segundo")
elif num1 < num2:
    print("El primer numero es menor al segundo")
else:
    print("los numeros son iguales")