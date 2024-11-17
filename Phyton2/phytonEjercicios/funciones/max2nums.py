def max(a, b):
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return print("Son numeros iguales")
num1 = int(input("Escribe un nº: "))
num2 = int(input("Escribe otro nº: "))

resultado = max(num1, num2)
print(f"El nº mayor es {resultado}")