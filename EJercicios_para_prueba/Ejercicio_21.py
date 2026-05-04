edad = int(input("Ingrese su edad:"))

if edad < 12:
    print(f"Edad: {edad}")
    print("Niño: pasa gratis")
elif edad <=17:
    print(f"Edad: {edad}")
    print("Adolesente: media tarifa")
elif edad <= 64:
    print(f"Edad: {edad}")
    print("Adulto: tarifa completa")
else: 
    print(f"Edad: {edad}")
    print("Adulto mayor: media tarifa")