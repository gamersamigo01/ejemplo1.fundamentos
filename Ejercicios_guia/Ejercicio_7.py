url = input("Write down the url of your web page: ")

if url.startswith("https://") or url.startswith("http://"):
    sin_protocolo = url.split("://")[1] #El url.split("://")[1] significa que el input del usuario se parte en 2 desde el "://" o sea "https://holaamigo.com/imagenes" quedaria ["https" , "holaamigo.com/imagenes"] y el [1] dice que solo se lea la parte derecha del split o sea "holaamigo.com/imagenes"
    if "/" in sin_protocolo:
        dominio = sin_protocolo.split("/")[0]#Aqui se hace otro split("/") que ocupando el ejemplo anterior quedaria ["holaamigo.com" , "imagenes"] y el [0] lee solo la parte izquierda del url o sea "holaamigo.com" dando asi el dominio
    else:
        dominio = sin_protocolo
    print(f"the domain is {dominio}")
elif url == "":
    print("Error write your url")
else:
    print("Error ingrese at the start apply the http:// or http:// to work")