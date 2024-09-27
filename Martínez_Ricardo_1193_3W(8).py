print(" ")
print("Martínez Estrada Ricardo / NO. de control: 1193 / Grupo 3°W.")
print(" ")

# Función para calcular el factorial de un número entero
def calcular_factorial(n):
    if n < 0:
        return None  # El factorial no está definido para números negativos
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Función para solicitar un número entero
def obtener_numero_entero():
    while True:
        numero = input("Digite un número entero no negativo: ")
        try:
            numero = int(numero)
            if numero < 0:
                print("Por favor, ingresa un número entero no negativo.")
            else:
                return numero
        except ValueError:
            print("Por favor, ingresa un número entero válido.")

# Obtener el número entero
numero = obtener_numero_entero()

# Calcular el factorial
resultado = calcular_factorial(numero)

# Mostrar el resultado
print ("El factorial de", numero, "es: ", resultado)