import random
import sys

guesses = 0
erraten = False

def randomNumber():
    global number
    number = str(random.randint(1, 9))


def identify():
    global erraten
    global guesses
    if guessed == number:
        erraten = True
        return("Du hast die Zahl " + number + " erraten!")
    elif guessed < number:
        guesses += 1
        return("Die Zahl ist größer als " + guessed)
    elif guessed > number:
        guesses += 1
        return("Die Zahl ist kleiner als " + guessed)
    else:
        print("fehler")


    


def anotherGame():
    global erraten
    global guesses
    answer = str(input("Willst du noch eine Runde spielen? j/n "))
    if answer == "j":
        randomNumber()
        erraten = False
        guesses = 0
        identify()
    elif answer == "n":
        sys.exit()
    else:
        global falschEingabe
        falschEingabe = True
        print("Fehler in anotherGame!!!")
    

    
randomNumber()

def erratenPrüfung():
    global guessed
    while erraten != True:
        guessed = input("Rate eine Zahl zwischen 1 - 9: ")
        print(identify())

erratenPrüfung()

if erraten:
    print("Du hast " + str(guesses) + " Versuche gebraucht.")
    anotherGame()



def wrongInput():
    global answer
    if falschEingabe:
        print("Sie haben etwas falsches eingegeben.")
        answer = str(input("Willst du noch eine Runde spielen? j/n"))