print("Pizzeria don pancho")

dinero = int(input("Introduzca el dinero que tiene disponible para comprar: "))

ingredientes_extra = ["+tomate","+salchicha","+salame","+piña"]

pizza = input("Ingrese la pizza que quiera elegir (napolitana,hawaiana o pepperoni): ")
total_ingredientes = 0
#Pizzas
napolitana = 5000
hawaiana = 7500
pepperoni = 6500

#Ingredientes
tomate = 300
salchicha = 800
salame = 500
piña = 350

if pizza == "napolitana":
    pizza = napolitana
elif pizza == "hawaiana":
    pizza = hawaiana
elif pizza == "pepperoni":
    pizza = pepperoni

print(f"El costo hasta ahora es de {pizza}")

Mas = input("Le gustaria agregarle ingredientes extra? s/n: ")

if Mas == "s":
    for ingredientes in ingredientes_extra:
        que_ingrediente = input("Cuales ingredientes usted quiere agregar (tomate, salchicha, salame, piña o digite salir): ")
        if que_ingrediente == "salir":
            break
        while que_ingrediente != "salir":
            if que_ingrediente == "tomate":
                total_ingredientes += tomate
            elif que_ingrediente == "salchicha":
                total_ingredientes += salchicha
            elif que_ingrediente == "salame":
                total_ingredientes += salame
            elif que_ingrediente == "piña":
                total_ingredientes += piña
            else:
                print("no esta dentro de las opciones")
            total_dinero = total_ingredientes + pizza
            if total_dinero > dinero:
                print("Supera su presupuesto")
            que_ingrediente = input("Cuales ingredientes usted quiere agregar (tomate, salchicha, salame, piña o digite salir): ")

print(f"Su pizza estar lista en unos minutos, esta tuvo el valor de {total_dinero}")
            

        