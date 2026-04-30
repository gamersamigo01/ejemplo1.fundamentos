edad = int(input("Ingrese su edad: "))

if edad >= 18 and edad > 0:
    print(f"Su edad {edad} es mayor de 18 años")
elif edad <= 0:
    print("Tiene que tener mas de 1 año de vida")
else:
    print("Usted es menor de edad")

edad_mayor = edad + 5
print(f"Su edad {edad} en 5 años será de {edad_mayor}")