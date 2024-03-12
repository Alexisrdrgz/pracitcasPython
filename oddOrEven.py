def odd_or_even(number):
    if number % 2 == 0:
        return "¡Es un número par!"
    else:
        return "¡Es un número impar!"

try:
    user_number = int(input("Ingresa un número: "))
    print(odd_or_even(user_number))
except ValueError:
    print("Por favor, ingresa un número válido.")
