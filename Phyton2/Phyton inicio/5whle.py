print("NÚMEROS MAYORES QUE 5")
print("---------------------")
lis = [1,1,1,1,1]
cont = 0
mayor = 0
while cont <=4:
    lis[cont] = int(input("Dame un numero: "))
    cont = cont+1
print(f"{lis}")
i = 0
mayores_o_iguales_a_cinco = 0

while i < len(numeros):
    if numeros[i] >= 5:
        mayores_o_iguales_a_cinco += 1
    i += 1