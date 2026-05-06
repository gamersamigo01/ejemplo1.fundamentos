import random
import string
longitud = int(input("Ingrese la longitud deseada para su contraseña: "))
caracteres = string.ascii_lowercase + string.digits
contraseña = ''.join(random.choice(caracteres) for i in range(longitud))

print(f"Su contraseña generada: {contraseña}")