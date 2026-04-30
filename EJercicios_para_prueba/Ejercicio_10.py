caracter = input("Ingrese un caracter: ").lower()


if len(caracter) != 1:
    print("tiene que ser un solo caracter")
else:
    if caracter in "aeiou": #Tiene que ser caracter in "aeiou" y no al revez
        print("Su caracter es una vocal")
    elif not caracter.isalpha():
        print("Su caracter no es una letra")
    else:
        print("Su caracter es una consonante")