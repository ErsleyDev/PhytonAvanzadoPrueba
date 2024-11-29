print("MENÚ")
print("____________________")
print("1. Introdudir datos")
print("2. Leer datos existentes")
print("3. Salir")
opc = int(input("Introduce una opción: "))
while opc != 3:
    if opc == 1:
        for i in range(1):
            ruta = "/home/erschilon/Documentos/PhytonAvanzadoPrueba/Phyton2/phytonEjercicios/Ficheros/txtFiles/nombreCompleto.txt"
            with open(ruta, mode="w", encoding="utf-8")as fichero:
                name = input("Escribe tu nombre completo: ")
                print(f"{name}", file=fichero)

                fichero.close()
while opc != 3:
    if opc == 2:
        ruta = "/home/erschilon/Documentos/PhytonAvanzadoPrueba/Phyton2/phytonEjercicios/Ficheros/txtFiles/nombreCompleto.txt"
        with open(ruta, mode="r", encoding="utf-8")as fichero:
            for line in fichero:
                print(line)
            fichero.close