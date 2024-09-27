print(" ")
print("Martínez Estrada Ricardo / NO. de control: 1193 / Grupo 3°W.")
print(" ")

# Función para solicitar un número entero
def obtener_numero_entero():
    while True:
        numero = input("Digite un número entero: ")

        # Comprobar si el número es un entero
        try:
            numero = int(numero)
            return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# Obtener el número entero
numero = obtener_numero_entero()

# Verificar condiciones
if numero > 40 and numero % 7 == 0:
    print("El número", numero, "es mayor que 40 y es divisible por 7.")
else:
    print("El número", numero, "no cumple las condiciones.")