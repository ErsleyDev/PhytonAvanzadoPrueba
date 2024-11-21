def cantLetra(palabra, letra):
    palabra = palabra.lower()
    letra = letra.lower()
    return palabra.count(letra)
x = input("Introduce una palabra: ")
y = input("Introduce una letra: ")
resultado = cantLetra(x, y)
print(f"La letra [{y}] aparece en la palabra {resultado} veces.")