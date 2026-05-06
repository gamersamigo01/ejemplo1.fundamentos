edad = int(input("Ingrese su edad: "))

if edad < 0 and edad > 120:
    print("Error. Variable de edad muy pequeña o muy grande")
else:
    print(f"Su edad: {edad}, se ha guardado")