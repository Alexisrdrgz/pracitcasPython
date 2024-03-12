import random

def play_rps(user_choice):
    options = ["piedra", "papel", "tijeras"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        return "¡Empate!"
    elif (user_choice == "piedra" and computer_choice == "tijeras") or (user_choice == "papel" and computer_choice == "piedra") or (user_choice == "tijeras" and computer_choice == "papel"):
        return f"Ganaste. La computadora eligió {computer_choice}."
    else:
        return f"Perdiste. La computadora eligió {computer_choice}."

user_input = input("Elige piedra, papel o tijeras: ").lower()
print(play_rps(user_input))
