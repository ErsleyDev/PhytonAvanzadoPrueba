import random
print("DADO")
print("___________________")
num = int(input("Cuantas tiradas quieres hacer: "))
if num <= 0:
    print("[ERROR]")
cont = 0
for i in range(num):
    num2=random.randint(1,6)
    print(f"Tirada {i+1}: {num2}")
    
    