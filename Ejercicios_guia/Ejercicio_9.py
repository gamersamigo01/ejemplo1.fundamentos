codigo = input("Ingrese su codigo (recuerde que los 4 digitos finales son numericos): ").strip().upper()
if codigo.startswith("PROD") and len(codigo) == 9 and codigo[5:].isdigit: #No es necesario un .(endswith) solo ocupando el codigo[5:] empieza a leer desde despues del "-" y revisa si son todos numeros con .isdigit()
    print(f"Su codigo {codigo} se ha guardado")
elif not codigo[5:].isdigit():
    print("Error, los 4 datos finales no son numericos")
else:
    print("Error de syntaxis")