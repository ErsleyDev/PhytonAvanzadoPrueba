print("MENÚ")
print("____________________")
print("1. Introdudir datos")
print("2. Leer datos existentes")
print("3. Salir")

opc = int(input("Introduce una opción: "))
while opc != 3: 
    if opc <= 0 or opc >3:
        print("ERROR")
    else:
        
        if opc == 1:
                ruta = "txtFiles/nombreCompleto.txt"
                with open(ruta, mode="w", encoding="utf-8")as fichero:
                    name = input("Escribe tu nombre completo: ")
                    print(f"{name}", file=fichero)
                    

        elif opc == 2:
            ruta = "txtFiles/nombreCompleto.txt"
            with open(ruta, mode="r", encoding="utf-8")as fichero:
                for line in fichero:
                        print(line)
    opc = int(input("Introduce una opción: "))

print("ADIÓS")
