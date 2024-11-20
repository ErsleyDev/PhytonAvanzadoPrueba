def finde(lista):
    if "Sábado" in lista or "Domingo" in lista:
        return True
    else:
        return False


cont=0
dia=["a", "b", "c"]
while cont<3:
    dia[cont] = input("Día: ")
    cont += 1


