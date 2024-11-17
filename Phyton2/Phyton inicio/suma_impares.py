print("SUMA IMPARES")
print("----------------------")
num = int(input("Escribe un nº: "))
if num<0:
    print("[ERROR]")
cont = 1
fact = 0
while cont<=num:
    fact = fact+cont
    cont = cont+2
print(f"{fact}")