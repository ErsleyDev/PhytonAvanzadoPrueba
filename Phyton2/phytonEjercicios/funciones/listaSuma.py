import random

def crear():
    lista1 = []
    for i in range(4):
        lista1.append(random.randint(1,20))
    return lista1

def suma(a,b):
    lista = []
    for i in range(4):
        x = a[i]+b[i]
        lista.append(x)
    return lista
    
l1 = crear()
l2 = crear()

print(l1,l2)

resultado = suma(l1,l2)
print(resultado)