num = int(input("Gib eine Nummer zum teilen ein: "))

listRange = range(2, num + 1)

divisorList = []

for number in listRange:
    if num%number == 0:
        divisorList.append(number)

print("Teiler ohne Rest:", divisorList)