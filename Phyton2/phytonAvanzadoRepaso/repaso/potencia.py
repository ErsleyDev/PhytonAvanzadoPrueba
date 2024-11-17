print("POTENCIA")
base = int(input("Introcue la base: "))
exponente = int(input("Introduce el exponenete: "))
if exponente > 0:
    resultado = 1
    for i in range(exponente):
        resultado = resultado * base
    print(f"{base} elevado a {exponente} = {resultado}")
else:
    print("ERROR")