ruta = "pyEjercicoFinal/txt/IESOrriolsEst.txt"
print("REGISTRO DEL ALUMNADO DEL IES ORRIOLS")
print("****************************************")
print()
print()
def menu():
    print("MENÚ PRINCIPAL")
    print("_________________________")
    print("1. INTRODUCCIÓN DE DATOS")
    print("2. MOSTRAR DATOS DE TODOS LOS ALUMNOS")
    print("3. MOSTRAR DATOS DE UN ALUMNO (NIA)")
    print("4. ESTADÍSTICAS. mostrar la nota media de un alumno")
    print("5. SALIR")
    
def entradaDatos():
        nia = int(input("NIA del alumno: "))
        nom = input("Nombre y primer apellido del alumno: ")
        print("Introduce las notas de Valenciano, Castellano, Inglés, Filosofía e Historia")
        lnomasig=["Valenciano", "Castellano", "Inglés", "Filosofía", "Historia"]
        lnotas = []
        for i in range(5):
            notas = int(input(f"Introduce la nota de {lnomasig[i]}: "))
            lnotas.append(notas)
        with open(ruta, mode="a", encoding="utf-8") as fichero:
            print(f"{nia} {nom} {lnotas}", file=fichero)

def mostrarDatos():
    with open(ruta, mode="r", encoding="utf-8") as fichero:
        for line in fichero:
            print(line)

def devolverLineaDatosAl():
    nia = int(input("Introduce el NIA que deseas buscar"))
    with open(ruta, mode="r", encoding="utf-8") as fichero:
        for line in fichero:
            


opc = 0
while opc != 5:
    menu()
    opc = int(input("Elige la opcion: "))
    if opc == 1:
        entradaDatos()
    elif opc == 2:
        print(" ")
        print("DATOS DEL ALUMNADO")
        mostrarDatos()
    elif opc == 3:
        devolverLineaDatosAl()
        
        
print("Hasta luego")