horas = int(input("Ingrese cuantas horas va a estar: "))
vehiculo = int(input("Ingrese que tipo de vehiculo va a estacionar (1=auto, 2=moto, 3=camion): "))
precio_base = 2000 * horas

if horas > 12:
    print("Maximo 12 horas permitido")
elif vehiculo == 1 and horas >= 3:
    total = (precio_base * 0.90) 
elif vehiculo == 2:
    total = (precio_base * 0.50) 
elif vehiculo == 3:
    total = (precio_base * 1.30) 
elif vehiculo == 1 and horas < 3:
    total = precio_base

print(f"Horas: {horas}")
print(f"Tipo: {vehiculo}")
print(f"Total a pagar: {total}")
