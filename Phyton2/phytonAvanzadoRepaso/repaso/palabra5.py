x = input("Escribe una palabra de 5 letras: ")
if len(x) == 5:
    print("CORRECTO")
    letra = input("Escribe una letra: ")
    cont = 0
    i = 0
    while i < len(x):
        if x[i] == letra:
            cont = cont+1
        i = i+1
    if cont > 0:
        print(f"La palabra {x} tiene la letra ({letra}) {cont} vez/veces")
    else:
        print(f"La palabra no contiene la letra {letra}")
    
else:
    print("ERROR")



while letra in x:
    cont = cont +1