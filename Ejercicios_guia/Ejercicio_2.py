contraseña = input("Ingrese su contraseña: ")

if len(contraseña) >= 8 and not contraseña.isalpha() and not contraseña.isnumeric() and contraseña.find(" ") == -1:
    print("Contraseña fuerte")
elif len(contraseña) < 8:
    print("Contraseña muy corta")
else:
    print("Error de formato")