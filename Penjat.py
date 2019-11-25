print("P E N J A T")
Palabras = ["arfil", "cartes", "casa", "silla", "menjador", "roberto", "ecologista", "veredicte", "poma", "electrocardioencefalogrames", "nicenoconstantinopolitanes", "additivomultiplicatives", "carbonatohidroxilapatites"]
Intentos = ['''
   +---+
   |   |
       |
       |
       |
       |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

Intento = []

Num = random.randint(0, len(Palabras) - 1)
Palabra = Palabras[Num]
error = 0
Aciertos = []
Mal = []
print("La paraula té " + str(len(Palabra)) + " lletres")
print(Intentos[0])
print("Introdueix una lletra")
Ganar = False
while error < len(Intentos) and not Ganar:
    Bien = False
    Intento = input()
    x = 0
    Sortir = False

    if Intento in Aciertos:
        print('NO HAS DE REPETIR LLETRES')
        error += 1
        print(Intentos[error])


    else:

        while x < len(Palabra):
            if Intento == Palabra[x]:
                print(Palabra[x], end=' ')
                Aciertos.append(Intento)
                Bien = True
            else:
                Acertados = 0
                Sortir = False
                while Acertados < len(Aciertos) and not Sortir:
                    if Palabra[x] == Aciertos[Acertados]:
                        print(Palabra[x], end=' ')
                        Sortir = True
                    Acertados += 1
            if not Sortir:
                print("_", end=' ')
                Sortir = True
            x += 1

        if not Bien:
            error += 1
            print(Intentos[error])
            print("La lletra " + Intento + " no és correcta!")
            if Intento not in Mal:
                Mal.append(Intento)
            else:
                print("No has de repetir lletres!")

    if error == 6:
        print("Has perdut!!!")
        Ganar = True

    if len(Aciertos) == len(Palabra):
        print("Has guanyat!")
        break
    print("Errors: " + str(error))
    print("Les lletres " + str(Mal) + " no es troben a la paraula.")

