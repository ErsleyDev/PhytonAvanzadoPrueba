print("DATOS DEL USUARIO")
print("_______________________")
print("Introduce los siguientes datos:")
nom = input("Nombre: ")
apell = input("Apellido: ")
#dd/mm/aaaa
fecha = input("Fecha de nacimiento: ")
mail = input("Corrreo Electrónico: ")

ruta = "txtFiles/datos.txt"
with open(ruta, mode="a", encoding="utf-8")as fichero:
    print(f"{nom} {apell} {fecha} {mail}", file=fichero)