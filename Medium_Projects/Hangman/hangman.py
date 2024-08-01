import numpy as np
import man_paint as mp
def randomWord():
    import requests, random, unidecode
    site = 'https://raw.githubusercontent.com/JorgeDuenasLerin/diccionario-espanol-txt/master/0_palabras_todas.txt'
    words = requests.get(site).content.splitlines()
    return unidecode.unidecode(random.choice(words).decode("utf-8"))
while True:
    word = randomWord()
    final, wordL, wrongL = ['_']*len(word), word.split(), []
    mp.colorear(0)
    while True:
        print('Una palabra de ' + str(len(word)) + ' letras:')
        print(np.array(final))
        print(" Y tus letras falladas han sido: ")
        print(np.array(wrongL))
        letter = input("Nueva letra: ").lower()
        print('\n')
        util, solution = 0, 0
        for i in range(len(word)):
            if word[i] == letter:
                final[i] = letter
                util += 1
        if util == 0:
            if letter in wrongL:
                print("Ya has dicho esa letra!\nPrueba con otra...", end="\n\n")
            else:
                wrongL += letter
                mp.colorear(len(wrongL))
                if len(wrongL) == 6:
                    print("Has perdido... \nLa palabra era: " + word)
                    print("Y has tenido " + str(len(wrongL)) + " fallos.")
                    break
        if final.count('_') == 0:
            print("¡¡¡Has ganado!!! \nEfectivamente la palabra era: " + word)
            print("Y has tenido " + str(len(wrongL)) + " fallos.")
            break
    input("Press enter to exit...")
