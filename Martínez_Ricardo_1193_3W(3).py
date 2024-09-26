# Exámen 1er parcial.
print(" ")
print("Martínez Estrada Ricardo / NO. de control: 1193 / Grupo 3°W.")
print(" ")

num1 = float(input("Digite el primer valor: "))
num2 = float(input("Digite el segundo valor: "))

# Determinar el menor de los dos valores
if num1 < num2:
    print(num1, "es menor que", num2)
else:
    print(num2, "es menor que", num1)

# Sumar los dos números
suma = num1 + num2
print("La suma de", num1, "y", num2, "es:", suma)