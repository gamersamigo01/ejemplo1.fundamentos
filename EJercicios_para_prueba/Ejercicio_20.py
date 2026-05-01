nombre = input("Ingrese su nombre: ").title()
edad = int(input("Ingrese su edad: "))
ciudad = input("Ingrese su ciudad: ")

#Informacion de trabajo

Horas_trabajo = int(input("Ingrese cuantas horas trabajo: "))
Valor_por_hora = int(input("Ingrese el pago de su trabajo por hora: "))

#Calculos
Salario_bruto = Horas_trabajo * Valor_por_hora

if Salario_bruto > 1000:
    Salario_impuesto = Salario_bruto * 0.80

if edad < 18 or edad > 65:
    Salario_impuesto *= 0.95

print(f"Nombre: {nombre}")
print(f"Ciudad: {ciudad}")
print(f"Edad: {edad}")
print(f"Salario neto final: {Salario_impuesto:.2f}")
