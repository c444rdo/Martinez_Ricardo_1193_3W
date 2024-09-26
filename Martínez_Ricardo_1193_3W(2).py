# Exámen 1er parcial.
print (" ")
print ("Martínez Estrada Ricardo / NO. de control: 1193 / Grupo 3°W.")
print (" ")

# Lectura de valores
a = input ("Digite el primer valor: ")
b = input ("Digite el segundo valor: ")
c = input ("Digite el tercer valor: ")

# Convertir los valores a a enteros (o a float si es necesario).
a = float (a)
b = float (b)
c = float (c)

# Comprobar si los valores son distintos
if a == b or b == c or a == c:
    print("Los valores introducidos deben de ser distintos. Introduciste 2 valores iguales.")
else:
    # Encontrar el mayor y el menor
    mayor = max(a, b, c)
    menor = min(a, b, c)
    
    print ("El mayor valor es:", mayor)
    print ("El menor valor es:", menor)