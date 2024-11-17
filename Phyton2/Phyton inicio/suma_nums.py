print("SUMA NUMEROS")
print("__________________")
cant = int(input("Cuantos numeros vas a introducir: "))
if cant <= 0:
    print("ERROR")
else:
    suma = 0
    for i in range(cant):
        num1 = int(input("Dime un nº: "))
        suma = suma + num1
    print(suma)
   
        
   