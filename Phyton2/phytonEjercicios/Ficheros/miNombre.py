ruta = "/home/erschilon/Documentos/PhytonAvanzadoPrueba/Phyton2/phytonEjercicios/Ficheros/txtFiles/niNombre.txt"
with open(ruta, mode="w", encoding="utf-8") as fichero:
    name = input("Cómo te llamas?: ")
    print(f"{name}", file=fichero)