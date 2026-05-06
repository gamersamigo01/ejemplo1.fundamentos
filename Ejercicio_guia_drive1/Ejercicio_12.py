n = int(input("Ingrese un numero entero: "))
sumas_pares = 0
for i in range(1,n+1):
    if i % 2 == 0:
        sumas_pares += 1
print(f"En {n} hay un total de {sumas_pares} pares")