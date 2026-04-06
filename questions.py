import random

categorias = {
    "Lenguaje": ["python", "programa", "variable"],
    "Estructuras": ["funcion", "bucle", "cadena"],
    "Tipos": ["entero", "lista", "cadena"],
}

print("Categorías disponibles:")
for categoria in categorias:
    print(f"- {categoria}")

categoria = input("Seleccioná una categoría: ")
if categoria not in categorias:
    print("Categoría no válida.")
    exit()

palabras = random.sample(categorias[categoria], len(categorias[categoria]))
puntaje = 0

print("¡Bienvenido al Ahorcado!")
print()

for word in palabras:
    guessed = []
    attempts = 6

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            puntaje += 6
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        letter = input("Ingresá una letra: ")

        if len(letter) != 1 or not letter.isalpha():
            print("Entrada no válida")
            continue

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("¡Bien! Esa letra está en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            puntaje -= 1
            print("Esa letra no está en la palabra.")
        print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
        puntaje = 0

    seguir = input("¿Querés jugar otra ronda? (s/n): ")
    if seguir != "s":
        break

print(f"Tu puntaje final es: {puntaje}")
