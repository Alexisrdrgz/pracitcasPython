def is_palindrome(palabra):
    palabra_limpia = palabra.lower().replace(" ", "")
    return palabra_limpia == palabra_limpia[::-1]

palabra_Completo = input("Ingresa una palabra o frase: ")
if is_palindrome(palabra_Completo):
    print("¡Es un palíndromo!")
else:
    print("No es un palíndromo.")
