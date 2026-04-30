comentario = input("Ingrese su comentario: ")

if comentario.strip() == "":
    print("error: ingrese alguna palabra")
elif "tonto" in comentario.lower() or "feo" in comentario.lower():
    limpio = comentario.replace("tonto", "*****").replace("feo","***")
    print(f"Su comentario es {limpio}")
else:
    print("Error de syntaxis")
