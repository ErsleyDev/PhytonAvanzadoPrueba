print("CÁCULO DEL FACTOIRAL DE UN Nº")
print("------------")
num = int(input("Escribe un nº: "))
fact = 1
if num <= 0:
    print("ERROR")
else:
    for i in range(num):
        fact = fact * (i+1)
print(f"El factorial de {num} es {fact}")