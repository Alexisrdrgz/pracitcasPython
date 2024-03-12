def acronym_generator(frase):
    palabras = frase.split()
    acronimo = "".join(palabra[0].upper() for palabra in palabras)
    return acronimo

palabra_completa = input("Ingresa una frase: ")
print(f"El acrónimo es: {acronym_generator(palabra_completa)}")
