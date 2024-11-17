def maxLong(a, b):
    if len(a) > len(b):
        return a
    else: 
        return b

p1 = input("Introduce la primera palabra: ")
p2 = input("Introduce la segunda palabra: ")

resultado = maxLong(p1, p2)
print(f"{resultado} tiene más letras")