userWord = input("Dein Name / Wort: ")
userWord = userWord.lower()

backward = []

for letter in reversed(userWord):
    backward.append(letter)


if list(userWord) == backward:
    print("\nDer Name/das Wort '" + userWord.capitalize() + "' ist ein Palindrom.")
    print("\n Def: Ein Palidrom ist eine sinnvolle Folge von\n Buchstaben, Wörtern oder Versen, die vorwärts- wie\n rückwärtsgelesen [den gleichen] Sinn ergeben.\n")
else:
    print("\nDer Name/das Wort '" + userWord.capitalize() + "' ist kein Palidrom.")
    print("\n Def: Ein Palidrom ist eine sinnvolle Folge von\n Buchstaben, Wörtern oder Versen, die vorwärts- wie\n rückwärtsgelesen [den gleichen] Sinn ergeben.\n")
