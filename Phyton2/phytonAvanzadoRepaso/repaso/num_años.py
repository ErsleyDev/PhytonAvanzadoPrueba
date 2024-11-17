print("AÑOS")
year = int(input("Escribe tu año de nacimiento: "))
if year > 2020 or year <  1930:
    print("[ERROR]")
else:
    print(f"Tienes {2024-year} años")