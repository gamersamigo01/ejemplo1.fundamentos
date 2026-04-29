usuario = input("Ingrese su nombre de usuario (tiene que tener mas de 5 letras y menos de 15): ")

if len(usuario) > 5 and len(usuario) < 16 and usuario[0].isalpha() and usuario.isalnum():
    print(f"Su nombre de usuario {usuario} se ha registrado correctamente")
elif len(usuario) < 5 and len(usuario) > 15:
    print("Error de longitud")
elif not usuario.isalpha() and usuario.isalnum():
    print("error de formato") 