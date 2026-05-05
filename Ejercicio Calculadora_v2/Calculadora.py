print("¡Bienvenido a la calculadora de python!")
while True:
    opcion = int(input("Ingrese una opcion (1-12): "))
    if opcion >=1 and opcion <= 8:
        texto = input("Ingrese un texto: ")        
        if opcion == 1:
            print(f"Su texto en mayusculas: {texto.upper()}")
        elif opcion == 2:
            print(f"Su texto en minusculas: {texto.lower()}")
        elif opcion == 3:
            print(f"¿Su texto es de digitos?: {texto.isdigit()}")
        elif opcion == 4:
            print(f"¿Su texto es alfabetico?: {texto.isalpha()}")
        elif opcion == 5:
            print(f"¿Si su texto tiene la palabra a, en que pocision esta?: {texto.find('a')}")
        elif opcion == 6:
            print(f"Su texto separado como lista: {texto.split()}")
        elif opcion == 7:
            print(f"El largo de su texto es de: {len(texto)} letras")
        elif opcion == 8:
            print(f"Su texto con todas las primeras letras despues de un espacio con mayusculas: {texto.title()}")
    elif opcion == 9:
        num1 = float(input("Ingrese su primer numero: "))
        num2 = float(input("Ingrese su segundo numero: "))
        opt = input("Ingrese la opcion que desea calcular(+,-,*,/ o %): ")
        
        if opt == "+":
                resultado = num1 + num2
                print(f"Suma: {resultado}")
        elif opt == "-":
                resultado = num1 - num2
                print(f"Resta: {resultado}")
        elif opt == "*":
                resultado = num1 * num2
                print(f"Multiplicacion: {resultado}")
        elif opt == "/":
            if num2 != 0:
                resultado = num1 / num2
                print(f"Division: {resultado}")
            else:
                print("El divisor no puede ser 0")
        elif opt == "%":
            if num2 != 0:
                resultado = num1 % num2
                print(f"Resto: {resultado}")
            else:
                print("El divisor no puede ser 0")
        else:
            print("Error, ingrese alguno de los simbolos matematicos mostrados para seguir")
    elif opcion == 10:
        num1 = float(input("Ingrese el primer numero: "))
        num2 = float(input("Ingrese el segundo numeor: "))
        
        if num1 > num2:
            print(f"El numero {num1} es mayor al numero {num2}")
        elif num1 == num2:
            print(f"El numero {num1} es igual al numero {num2}")
        else:
            print(f"El numero {num1} es menor al numero {num2}")
        diferencia_absoluta = abs(num1 - num2)
        print(f"La diferencia entre los dos es de: {diferencia_absoluta}")
    elif opcion == 11:
        num1 = float(input("Ingrese su numero: "))
        if num1 % 2 == 0:
            print(f"Su numero {num1} es par")
        elif num1 % 2 == 1:
            print(f"Su numero {num1} es impar")        
    elif opcion == 12:
        print("Gracias, vuelva pronto")
        break
    else:
        print("Error, opcion no esta dentro de los parametros")