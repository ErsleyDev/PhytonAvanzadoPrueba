print("TABLA DE MULTIPLICAR")
print("_________________")
num = int(input("Dime un nº del 1 al 10: "))
cont = 10
if num <= 0 or num > 10:
    print("ERROR")
else:
    for i in range(1, cont + 1):  # Rango desde 1 hasta 10
        print(f"{num} x {i} = {num * i}")