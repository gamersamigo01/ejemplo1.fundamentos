print("Calculadora")

num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

opt = input("Ingrese una operacion matematica (+,-,*,/): ")
if opt == "+":
    suma = num1 + num2
    print(f"La suma de sus numeros es de: {suma}")
elif opt == "-":
    resta = num1 + num2
    print(f"La resta de sus numeros es de: {resta}")
elif opt == "*":
    mutli = num1 * num2
    print(f"El resultado de su multiplicacion es de: {mutli}")
elif opt == "/":
    if num2 != 0:
        division = num1 / num2
        print(f"El resultado de su division es de: {division:.1f}")
    else:
        print("No se puede dividir por 0")
else:
    print("Error, caracter no registrado")