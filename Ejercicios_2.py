palabra = input("Escriba una palabra: ")
cadena_invertida = palabra[::-1]

if cadena_invertida == palabra:
    print("Su palabra es palindromo")
else:
    print("Su palabra no es palindromo")