def suma(a,b):
    return a + b
def resta(a,b):
    return a - b
def multi(a,b):
    return a * b
def division(a,b):
    return a / b
    
num1 = int(input("Introduce el primer número: "))
num2 = int(input("Introduce el siguiente número: "))

print("S. Suma")
print("R. Resta")
print("M. Multiplicación")
print("D. División")

opcion = input("¿Qué operación quieres hacer?: ")

if opcion == "S" or opcion == "s":
    resultado = suma(num1, num2)
    print(f"{num1} + {num2} = {resultado}")
elif opcion == "R" or opcion == "r":
    resultado = resta(num1, num2)
    print(f"{num1} + {num2} = {resultado}")
elif opcion == "M" or opcion == "m":
    resultado = multi(num1, num2)
    print(f"{num1} + {num2} = {resultado}")
elif opcion == "D" or opcion == "d":
    resultado = division(num1, num2)
    print(f"{num1} + {num2} = {resultado}")


