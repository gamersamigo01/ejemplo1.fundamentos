num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

suma = num1 + num2
resta = num1 - num2
multiplica = num1 * num2

print("Ingrese la opcion para ver el resultado de la operacion: ")
print("1.suma")
print("2.resta")
print("3.Multiplicacion")
opt = int(input("opcion: "))

if opt == 1:
    print(f"El resultado de su suma es de: {suma}")
elif opt == 2:
    print(f"El resultado de su resta es de: {resta}")
elif opt == 3:
    print(f"El resultado de su multiplicacion es de: {multiplica}")
else:
    print("Error, no esta dentro del margen")
