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
    
opc = 0
while opc != 5:
    menu()
    opc = int(input("Elige la opcion: "))
    if opc == 1:
        nia = int(input("NIA del alumno: "))
        nom = input("Nombre y primer apellido del alumno: ")
        print("Introduce las notas de Valenciano, Castellano, Inglés, Filosofía e Historia")
        val = int(input("Nota de Valenciano: "))
        cas = int(input("Nota de Castellano: "))
        ing = int(input("Nota de Inglés: "))
        filo = int(input("Nota de Filosofía: "))
        hist = int(input("Nota de HIstoria: "))
        notas = [val, cas, ing, filo, hist]
print("hasta luego")

