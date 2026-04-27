def menu():
    print("#####Calculadora#####")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potenciar")
    print("6. Resto")
    print("7. Salir")


def sumar(opt,num1,num2):

    if opt ==1:
        resultado = num1 + num2
    elif opt ==2:
        resultado = num1 - num2
    elif opt == 3: 
        resultado = num1 * num2
    elif opt == 4:
        resultado = num1 / num2
    elif opt == 5:
        resultado = num1 ** num2
    elif opt == 6:
        resultado = num1 % num2
    
    
                    
    
    print(f"El resultado de su operacion es de {resultado}")
    return


