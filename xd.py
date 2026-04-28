print("Pizzeria don pancho")

dinero = int(input("Introduzca el dinero que tiene disponible para comprar: "))

ingredientes_extra = ["+tomate","+salchicha","+salame","+piña"]

pizza = input("Ingrese la pizza que quiera elegir (napolitana,hawaiana o pepperoni): ")

napolitana = 5000
hawaiana = 7500
pepperoni = 6500

if pizza == "napolitana":
    napolitana
elif pizza == "hawaiana":
    pizza = hawaiana
elif pizza == "pepperoni":
    pepperoni

print(f"El costo hasta ahora es de {pizza}")