print("ACCESO A FICHEROS")
print("_____________________________")
ruta = "txtFiles/10nums.txt"
with open(ruta, mode="r", encoding="utf-8") as fichero:
    i=1
    for line in fichero:
        if i==5:
            print(line)
            break
        else:
            i=i+1
