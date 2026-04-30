nombre = input("Ingrese su nombre: ")
año_nacimiento = int(input("Ingrese el año en que nacio: "))

años_usuario = 2025 - año_nacimiento #Tambien se puede hacer una variable de año_actual que se vaya actualizando cada año para hacer la resta automatica

if años_usuario >= 18:
    print(f"Bienvenido {nombre}")
else:
    print(f"Acceso restringido")