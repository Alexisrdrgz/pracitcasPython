def contador_Palabras(texto):
    palabras = texto.split()
    return len(palabras)

texto_Usuario = input("Ingresa una oración: ")
print(f"La oración tiene {contador_Palabras(texto_Usuario)} palabras.")
