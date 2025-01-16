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
    
def entradaDatos(nia, nom, val, cas, ing, filo, hist):
        nia = int(input("NIA del alumno: "))
        nom = input("Nombre y primer apellido del alumno: ")
        print("Introduce las notas de Valenciano, Castellano, Inglés, Filosofía e Historia")
        lnomasig=["Valenciano", "Castellano", "Inglés", "Filosofía", "Historia"]
        for i in range(5):
             
        val = int(input("Nota de Valenciano: "))
        cas = int(input("Nota de Castellano: "))
        ing = int(input("Nota de Inglés: "))
        filo = int(input("Nota de Filosofía: "))
        hist = int(input("Nota de HIstoria: "))
        notas = [val, cas, ing, filo, hist]

        with open(ruta, mode="a", encoding="utf-8") as fichero:
            print(f"{nia}, {nom}, {val}, {cas}, {ing}, {filo}, {hist}", file=fichero)

opc = 0
while opc != 5:
    menu()
    opc = int(input("Elige la opcion: "))
    if opc == 1:
        
        infoAlum = entradaDatos(nia, nom, val, cas, ing, filo, hist)
print("hasta luego")