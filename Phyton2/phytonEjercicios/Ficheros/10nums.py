import random
print("ACCESO A FICHEROS")
vm = int(input("Introduce el valor mínimo: "))
vM = int(input("Introduce el valor máximo: "))
ruta = "txtFiles/10nums.txt"
with open(ruta, mode="a", encoding="utf-8") as fichero:
    for i in range(10):
        num = random.randint(vm,vM)
        print(f"{num}", file=fichero)
