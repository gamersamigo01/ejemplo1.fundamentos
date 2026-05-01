n1 = int(input("N1: "))
n2 = int(input("N2: "))
n3 = int(input("N3: "))

positivos = 0 #Contador de positivos

if n1 > 0:
    positivos += 1
elif n2 > 0:
    positivos += 1
elif n3 > 0:
    positivos += 1
resultado = positivos >= 2 #Esta variable revisa si lo propuesto es verdadero

print(f"¿Al menos dos son positivos?: {resultado}")
    

