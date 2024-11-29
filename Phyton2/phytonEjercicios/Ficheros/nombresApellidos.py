ruta = "/home/erschilon/Documentos/PhytonAvanzadoPrueba/Phyton2/phytonEjercicios/Ficheros/txtFiles/nombreCompleto.txt"
with open(ruta, mode="w", encoding="utf-8")as fichero:
    name = input("Cómo te llamas: ")
    apell = input("Cómo es tu apellido: ")
    print(f"{name} {apell}", file=fichero)

    fichero.close()