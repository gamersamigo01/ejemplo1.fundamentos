print("Calculadora")
num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2

print(f"Resultado de su suma: {suma}")
print(f"Resultado de su resta: {resta}")
print(f"Resultado de su multiplicacion: {multiplicacion}")

if num2 != 0:
    division = num1 // num2
    print(f"Resultado de su division entera: {division}")
    
    residuo = num1 % num2
    print(f"El residuo de su division es de: {residuo}")
else:
    print("No puede dividir entre 0")