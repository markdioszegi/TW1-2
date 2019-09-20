from __future__ import print_function
import os
import time
import random
import datetime
import sys

hangmen = ['''
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
    =========''', '''
      +---+
      |   |
      X   |
     /|\  |
     / \  |
          |
    =========''']

startTime = 0

def printStatus(lives):
    if lives == 1:
        print(lives, " guess left!")
    else:
        print(lives, " guesses left.")
    print(" ".join(hangmen[7 - lives]))

def clearScreen():
    os.system("cls" if os.name == "nt" else "clear")

def readFromFile(filename):
    lines = []
    newLines = []
    with open(os.path.join(sys.path[0], filename), "r", encoding="UTF-8") as f:
        lines = f.readlines()
    for l in lines:
        l = l[:-1]
        newLines.append(l.split(" | "))
    f.close()
    return newLines

def evaluation(startTime, guesses, guessedWord):
    stopTime = time.time()
    guessingTime = round(stopTime - startTime)
    print("It took you {} seconds and {} guesses! Good job!".format(guessingTime, guesses))
    saveHighScore(guessingTime, guesses, guessedWord)

def saveHighScore(guessingTime, guesses, guessedWord):
    t = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(time.time()))
    name = input("Name: ")
    score = name
    with open(os.path.join(sys.path[0], "highscore.txt"), "a", encoding="UTF-8") as f:
        f.write("{} | {} | {} | {} | {}\n".format(name, t, guessingTime, guesses, guessedWord))
        f.close()
    #date = datetime.

def printBestScores():
    print("--- |High Score| ---")
    tmpScores = []
    scores = []
    topTen = []
    try:
        with open(os.path.join(sys.path[0], "highscore.txt"), "r", encoding="UTF-8") as f:
            tmpScores = f.readlines()
        for index, score in enumerate(tmpScores):
            tmpScores[index] = score.rstrip("\n")
            scores.append(score.split(" | "))
        for index, score in enumerate(scores):
            tmp = []
            avg = int(score[2]) + int(score[3]) / 2
            tmp.append(int(avg))
            tmp.append(int(index))
            topTen.append(tmp)
            #print(score[3])
        topTen.sort(key = lambda x: x[0])
        #topTen.sort()
        #print(topTen)
        i = 0
        while i < len(topTen) and i < 10:
            print(i + 1, ":", " | ".join(scores[topTen[i][1]]), end="")
            i += 1
    except:
        with open(os.path.join(sys.path[0], "highscore.txt"), "w", encoding="UTF-8") as f:
            f.write("")
        
def gameType():
    gtype = input("Capitals (1) or custom words (2)?")
    if gtype == "1":
        pass
    elif gtype == "2":
        pass
    else:
        print("Try again!")
    return gtype

def main():
    LIVES = 7
    #gameType()  #//TODO
    startTime = time.time()
    feladvanyok = []
    feladvanyok = readFromFile("capitals.txt")
    print(feladvanyok)

    randomNumber = random.randrange(0, len(feladvanyok))
    feladvany = feladvanyok[randomNumber][1]
    hint = feladvanyok[randomNumber][0]

    fade = []
    alreadyGuessedLetters = []

    for i in range(len(feladvany)):
        if feladvany[i] == " ":
            fade.append(" ")
        else:
            fade.append("_")

    print("het eleted van")
    print(feladvany)
    clearScreen()      #DEBUG

    while LIVES != 0 and fade != feladvany:
        printStatus(LIVES)
        print(*fade, sep="  ")
        solution = feladvany.lower()
        if LIVES == 1:
            print("Hint: The capital of {}".format(hint))
        letterGuess = input("Guess a letter or the whole word: ")
        letterGuess = letterGuess.lower()
        if letterGuess == solution:
            print("You win!")
            evaluation(startTime, len(alreadyGuessedLetters) + 1 + (7 - LIVES), feladvany)
            break
        elif letterGuess in solution:
            if not letterGuess in alreadyGuessedLetters:
                for i in range(len(solution)):
                    if solution[i] == letterGuess:
                        fade[i] = feladvany[i]
                        alreadyGuessedLetters.append(letterGuess)
            else:
                print("Already guessed that letter!")
                print("Letters guessed: {}".format(alreadyGuessedLetters))
                input("Press enter to continue...")
        elif len(letterGuess) > 1:
            print("That is not the whole word! (-2 health points)")
            input("Press enter to continue...")
            if LIVES == 1:
                LIVES -= 1
            else:
                LIVES -= 2
        else:
            LIVES -= 1
        if LIVES > 1:
            clearScreen()
            printStatus(LIVES)
        if LIVES == 0:
            clearScreen()
            print(" ".join(hangmen[7]))
            print("Game over! The word was: {}".format(feladvany))
            break
        if "".join(fade).lower() == solution:
                print("You win!")
                evaluation(startTime, len(alreadyGuessedLetters) + 1 + (7 - LIVES), feladvany)
                break
        clearScreen()
        #time.sleep(2)

    printBestScores()

    restart = (input("Do you want to play another game? (Yes/No) (y/n): ")).lower()
    if restart == "yes" or restart == "y":
        main()
    else:
        exit()

main()