def mad_libs():
    noun = input("Ingresa un sustantivo: ")
    adjective = input("Ingresa un adjetivo: ")
    verb = input("Ingresa un verbo en pasado: ")

    story = f"El {adjective} {noun} {verb} por el parque."
    print(story)

mad_libs()
