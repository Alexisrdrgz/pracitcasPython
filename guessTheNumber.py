import random

def guess_the_number():
    secret_number = random.randint(1, 100)
    attempts = 0

    while True:
        user_guess = int(input("Adivina el número (entre 1 y 100): "))
        attempts += 1

        if user_guess == secret_number:
            print(f"¡Correcto! El número era {secret_number}. Necesitaste {attempts} intentos.")
            break
        elif user_guess < secret_number:
            print("Intenta con un número más grande.")
        else:
            print("Intenta con un número más pequeño.")

guess_the_number()
