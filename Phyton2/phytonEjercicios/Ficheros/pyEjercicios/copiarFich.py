print("COPIAR FICHEROS")
print("_____________________________")
print("Ficha origen")
ruta = "txtFiles/copiarFich1.txt"
with open(ruta, mode="r", encoding="utf-8") as fichero:
    for line in fichero:
        print(line)
        print("ficha destino")
    with open(ruta, mode="w", encoding="utf-8")as fichero2:
        x = input("Copia la información: ")
        for line in fichero:
            print(line)