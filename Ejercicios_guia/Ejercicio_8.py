comentario = input("Ingrese su comentario: ")

if comentario.strip() == "": 
    print("error: ingrese alguna palabra")
elif "tonto" in comentario.lower() or "feo" in comentario.lower(): #Aca ocupas la funcion lower, asi el comentario que de el usuario no se transforma todo en lower, a diferencia de que si lo ponemos en el input
    limpio = comentario.replace("tonto", "*****").replace("feo","***") #Se ocupan 2 replaces diferentes para que funcione, pero pueden ser uno seguido de otro
    print(f"Su comentario es {limpio}")
else:
    print(f"Comentario publicado: {comentario}")
