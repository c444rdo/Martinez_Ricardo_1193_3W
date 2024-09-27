print(" ")
print("Martínez Estrada Ricardo / NO. de control: 1193 / Grupo 3°W.")
print(" ")

# Función para solicitar un número natural
def obtener_numero_natural():
    while True:
        numero = input("Digite un número natural: ")

        # Comprobar si el número es un entero y mayor o igual a 0
        try:
            numero = int(numero)
            if numero < 0:
                print("El número debe ser un número natural (0 o positivo). Inténtalo de nuevo.")
            else:
                return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# Obtener el número natural
numero = obtener_numero_natural()

# Determinar si el número es par o impar
if numero % 2 == 0:
    print("El número", numero, "es par.")
else:
    print("El número", numero, "es impar.")