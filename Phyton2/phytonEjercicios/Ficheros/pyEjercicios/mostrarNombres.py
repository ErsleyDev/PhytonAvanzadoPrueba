ruta = "/home/erschilon/Documentos/PhytonAvanzadoPrueba/Phyton2/phytonEjercicios/Ficheros/txtFiles/nombreCompleto.txt"
with open(ruta, mode="r", encoding="utf-8")as fichero:
    for line in fichero:
        print(line)
    fichero.close()