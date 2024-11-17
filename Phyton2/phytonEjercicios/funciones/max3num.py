def max(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
num1 = int(input("Escribe un nº: "))
num2 = int(input("Escribe otro nº: "))
num3 = int(input("Escribe otro nº: "))

resultado = max(num1, num2, num3)
print(f"El nº mayor es {resultado}")