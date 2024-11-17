numeros = []
contador = 0
print("Numero mayores que 5")
print("__________________________")
# Pedimos 5 números al usuario
while len(numeros) < 5:
    numero = float(input("Introduce un número: "))
    numeros.append(numero)

# Mostramos los números introducidos
print("Los números introducidos son:", numeros)

# Contamos cuántos números son mayores o iguales a 5
i = 0
mayores_o_iguales_a_cinco = 0

while i < len(numeros):
    if numeros[i] >= 5:
        mayores_o_iguales_a_cinco += 1
    i += 1

# Mostramos la cantidad de números mayores o iguales a 5
print("Cantidad de números mayores o iguales que 5:", mayores_o_iguales_a_cinco)