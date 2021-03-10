import random

print("H A N G M A N\n")
words = ['python', 'java', 'kotlin', 'javascript']
word = words[random.randint(0, len(words)-1)]
list_word = list(word)
setLetras = set()
guion = list(len(list_word) * "-")
indices = []
letter = ""
palabraMostrada = "".join(guion)
intentos = 8
menu = ""
start = "play"
salir = "exit"

while menu != start and menu != salir:
    menu = input('Type "play" to play the game, "exit" to quit: ')

if menu == start:
    while intentos > 0 and word != palabraMostrada:
        print("\n", end="")
        print(palabraMostrada)
        letter = input("Input a letter: ")
        letterUp = letter.lower()
        if letter.isalpha() and letter == letterUp and len(letter) == 1:
            if letter in list_word and letter not in setLetras:
                for i in range(len(list_word)):
                    if list_word[i] == letter:
                        indices.append(i)
                for index in indices:
                    guion[index] = letter

                indices = []
                setLetras.add(letter)

            elif letter in setLetras:
                print("You've already guessed this letter")

            else:
                print("That letter doesn't appear in the word")
                setLetras.add(letter)
                intentos = intentos - 1

            palabraMostrada = "".join(guion)

        else:
            if len(letter) > 1:
                print("You should input a single letter")
            else:
                print("Please enter a lowercase English letter")
    if palabraMostrada != word:
        print("You lost!")
    else:
        print(palabraMostrada)
        print("You guessed the word " + word + "!")
        print("You survived!")