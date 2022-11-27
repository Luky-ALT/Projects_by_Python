

text = """I've generated a random 4 digit number for you. 
Let's play a bulls and cows game."""

separate = "_ _" * 14
separate_1 = " " * 14


print("Welcome to Tic Tac Toe: ")
print(separate)
print("            GAME RULES:")
print(separate)
print("Lets start the game: ")
print(text)

import random

number = []
zivoty = 0
p=4

def MakeNumber():
    for i in range(4):
        x = random.randrange(0, 4)
        number.append(x)
    if len(number) > len(set(number)):
        number.clear()
        MakeNumber()


def PlayGame():
    global zivoty
    zivoty += 1
    cows = 0
    bulls = 0
    print(number)
    choice = input("Enter a 4 digit numbers: ")
    guess = []
    for i in range(4):
        guess.append(int(choice[i]))
    #for i in range(4):
    for j in range(4):
        if (guess[i] == number[j]):
              cows += 1
    for x in range(4):
        if guess[x]== number[x]:
            bulls += 1
    print("bulls: ", bulls)
    print("cows: ", cows)
    if (bulls == 4):
         print("Correct, you've guessed the right number in", p-(1),"guesses!")
    if (bulls != 4):
         PlayGame()

MakeNumber()
PlayGame()