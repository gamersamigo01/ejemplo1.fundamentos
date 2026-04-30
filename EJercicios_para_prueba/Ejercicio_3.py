contraseña = input("Ingrese su contraseña: ")
clave_correcta = "python123" #No es necesario hacer esta variable, pude ser if contraseña = "python123"


if contraseña == clave_correcta:
    acceso = True #Se debe declarar esta variable dentro del if
    print("Acceso concedido")
else:
    acceso = False
    print("Acceso denegado")

print(f"Variable de acceso: {acceso}")