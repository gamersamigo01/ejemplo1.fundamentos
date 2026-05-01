año = int(input("Ingrese un año para ver si es biciesto: "))

if (año % 4 ==0 and not año % 100 ==0) or año % 400== 0:
    print("Su año si es biciesto")
else:
    print("Su año no es biciesto")