print("HUCHA")
goal = int(input("¿Cuantos euros quieres ahorrar?: "))
if goal < 0:
    print("[ERROR]")
num2 = int(input("¿Cuantos euros quieres meter en la hucha?"))

while num2<goal:
    num=int(input("¿Cuantos euros quieres meter en la hucha?"))
    num2 = num2 + num
print(f"Objetivo conseguido, has ahorrado {num2}€")
    
