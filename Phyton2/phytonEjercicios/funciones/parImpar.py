def par(a):
    if a % 2 == 0:
        return True
    else:
        return False
num = int(input("Escribe un nº: "))
if par(num) is True:
    print(f"El numero {num} es PAR")
else:
    print("Es impar")