print("Pizzeria don pancho")

dinero = int(input("Introduzca el dinero que tiene disponible para comprar: "))

ingredientes_extra = ["+tomate","+salchicha","+salame","+piña"]

pizza = input("Ingrese la pizza que quiera elegir (napolitana,hawaiana o pepperoni): ")

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
    napolitana
elif pizza == "hawaiana":
    pizza = hawaiana
elif pizza == "pepperoni":
    pepperoni

print(f"El costo hasta ahora es de {pizza}")

Mas = input("Le gustaria agregarle ingredientes extra? s/n: ")

if Mas == "s":
    for ingredientes in ingredientes_extra:
        que_ingrediente = input("Cuales ingredientes usted quiere agregar (tomate, salchicha, salame, piña o digite salir): ")
        while que_ingrediente != "salir":
            if que_ingrediente == "tomate":
                total = pizza + tomate
                if total > dinero:
                    print("Esta fuera de su presupuesto")
        