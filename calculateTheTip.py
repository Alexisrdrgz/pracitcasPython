def calculo(total, porcentaje):
    cantidad_total = total * (porcentaje / 100)
    return cantidad_total

total = float(input("Ingresa el total de la cuenta: "))
porcentaje = float(input("Ingresa el porcentaje de propina que deseas dar: "))
print(f"La propina a pagar es: ${calculo(total, porcentaje):.2f}")
