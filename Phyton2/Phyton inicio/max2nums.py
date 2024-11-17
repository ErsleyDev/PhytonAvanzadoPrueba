def numMayor(a, b):
    if a > b:
        return a
    else:
        return b
num1 = int(input("Escribe un nº: "))
num2 = int(input("Escribe otro nº: "))

mayor = numMayor(num1, num2)
print(mayor)