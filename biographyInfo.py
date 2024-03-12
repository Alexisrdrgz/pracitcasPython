def biografia(nombre, edad, ocupacion):
    return f"{nombre} tiene {edad} años y trabaja como {ocupacion}."

nombre = input("Ingresa tu nombre: ")
edad = input("Ingresa tu edad: ")
ocupacion = input("Ingresa tu ocupación: ")

print(biografia(nombre, edad, ocupacion))
