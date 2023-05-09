#toto je subor obesenec.py
import os
from random import choice
import figurka


slovo = choice(["obesenec", "autobus", "klavesnica", "nedela"])
tajnicka = len(slovo) * ["_"]
zivoty = 7
hra_prebieha = True

while hra_prebieha and zivoty > 0:
  os.system("clear")
  print(figurka.hangman[7 - zivoty])
  print(f"Tajnicka: {' '.join(tajnicka)}", f"ZIVOTY: {zivoty}")
  hadanie = input("HADAJ PISMENO ALEBO CELE SLOVO: ").lower()


  if slovo == hadanie:
    hra_prebieha = False

  elif len(hadanie) == 1 and hadanie in slovo:
    for index, pismeno in enumerate(slovo):
      if pismeno == hadanie:
        tajnicka[index] = hadanie

    hra_prebieha = False if "_" not in tajnicka else True

  else:
    zivoty -= 1


if not hra_prebieha:
    print("SUPER, UHADOL SI TAJNE SLOVO!")

else:
    os.system("clear")
    print(figurka.hangman[7 - zivoty])
    print(f"PReHRAL SI, TAJNE SLOVO BOLO *{slovo}*")



