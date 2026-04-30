Base = int(input("Ingrese la base de su triangulo (solo numero entero): "))
altura = int(input("Ingrese la altura de su triangulo (solo numero entero): "))

Area_triangulo = Base * altura

if Area_triangulo > 100:
    print(f"El area de su triangulo es: {Area_triangulo}cm2, por lo tanto es grande")
else:
    print(f"El area de su triangulo es: {Area_triangulo}cm2, por lo tanto es pequeño")