cal_1 = int(input("Ingrese su primera calificacion (solo numeros enteros): "))
cal_2 = int(input("Ingrese su segunda calificacion (solo numeros enteros): "))
cal_3 = int(input("Ingrese su tercera calificacion (solo numeros enteros): "))

promedio = (cal_1 + cal_2 + cal_3)//3

if promedio >= 70:
    print(f"Su promedio es de {promedio}, Usted esta aprobado")
    estado = "Aprovado"
elif promedio >= 50 and promedio < 70:
    print(f"Su promedio es de {promedio}, Usted tiene que dar prueba de recuperacion")
    estado = "Recuperacion"
elif promedio < 50 and promedio >= 0:
    print(f"Su promedio es de {promedio}, usted esta reprobado")
    estado = "Reprovado"
else:
    print("Error escriba un numero entero positivo menor a 100")

print(f"Su estado: {estado}")