print(" ")
print("Martínez Estrada Ricardo / NO. de control: 1193 / Grupo 3°W.")
print(" ")

# Función para solicitar valores únicos
def obtener_valores_unicos():
    while True:
        a = input("Digite el primer valor: ")
        b = input("Digite el segundo valor: ")
        c = input("Digite el tercer valor: ")

        # Convertir los valores a float
        a = float(a)
        b = float(b)
        c = float(c)

        # Comprobar si los valores son distintos
        if a == b or b == c or a == c:
            print("Los valores introducidos deben de ser distintos. Introduciste 2 valores iguales. Inténtalo de nuevo.")
        else:
            return a, b, c

# Obtener los valores únicos
a, b, c = obtener_valores_unicos()

# Encontrar el mayor y el menor
mayor = max(a, b, c)
menor = min(a, b, c)

print("El mayor valor es:", mayor)
print("El menor valor es:", menor)