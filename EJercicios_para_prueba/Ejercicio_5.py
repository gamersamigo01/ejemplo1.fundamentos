valor_1 = input("Ingrese un valor (True o False): ").lower() #El lower para que el programa no tenga fallos por escribir true o false en mayusculas
valor_2 = input("ingrese el segundo valor (True o False): ").lower()


if valor_1 == "true": #Definir las variables como booleanas
    valor_1 = True
else:
    valor_1 = False
    
if valor_2 == "true":
    valor_2 = True
else:
    valor_2 = False   
    
resultado_and = valor_1 and valor_2
resultado_or = valor_1 or valor_2

print(f"{valor_1} AND {valor_2} = {resultado_and}")
print(f"{valor_1} Or {valor_2} = {resultado_or}")