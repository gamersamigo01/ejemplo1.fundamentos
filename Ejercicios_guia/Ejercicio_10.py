nombre = input("Ingrese su nombre: ").lower().strip()
apellido = input("Ingrese su apellido: ").lower().strip()


if nombre.isalpha() and apellido.isalpha() and len(nombre) > 0 and len(apellido) > 0:
    
    nombre_usuario = nombre[0] + apellido[0] #Con esto se guardan las dos iniciales del nombre y el apellido [0] la pocision 0 equivale a la primera letra
    print(f"{nombre_usuario}")

elif len(nombre) <= 0:
    print("Error, escriba algo")
else:
    print("Error, su nombre o apellido tiene numeros")
