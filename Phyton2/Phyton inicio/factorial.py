print("CÁLCULO DELL FACTORUAL DE UN Nº")
print("-------------------------------")
fact = 1
cont = 1
num = int(input("Escribe un Nº: "))
while cont<=num:
    fact=fact*cont
    cont=cont+1
print(f"El factorial de {num} es {fact}")
fact = 1
if numero <= 0:
    print("ERROR")
else:
    for i in range(1, numero + 1):
    fact = fact * i
    print(factorial)