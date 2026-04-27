from Funciones import menu,sumar

# Esta funcion da el menu de la calculadora
menu()

resultado = 0
num1 = 0
num2 = 0

opt = int(input("Ingrese la opcion que usted necesite"))

while opt != 7:
    if opt == 1:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        #La funcion sumar hace que de el resultado de cada operacion dependiendo de la opcion que utilizemos
        sumar(opt,num1, num2)
    elif opt == 2:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
    
        sumar(opt,num1,num2)
    elif opt == 3:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        sumar(opt,num1,num2)
    elif opt == 4:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        sumar(opt,num1,num2)
    elif opt == 5:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        sumar(opt,num1,num2)
    elif opt == 6:
        num1 = int(input("Ingrese el primer numero: "))
        num2 = int(input("Ingrese el segundo numero: "))
        
        sumar(opt,num1,num2)
    elif opt == 7:
        print("Gracias por usar el programa")
        break
    else:
        print("comando mal usado, intente otra vez")
    menu()
    opt = int(input("Ingrese la opcion que usted nececite"))

    
    
    
    