import random
import csv

emptyList = []
fullList = []

def listComprehension():
    a = list(random.sample(range(80), random.randint(10, 20)))
    b = list(random.sample(range(80), random.randint(10, 20)))

    checkList = [item for item in a if item in b]

    if len(checkList) == 0:
        emptyList.append(checkList)
    else:
        fullList.append(checkList)

def writeCVS():

    rounds = 0
    while rounds < 1000:
        listComprehension()
        rounds += 1

    with open("Excel/comprehension.csv", "r") as compareRoundsFile:
        reader = csv.reader(compareRoundsFile)

    print(reader)

    '''if reader 
     
    with open("Excel/comprehension.csv", "a") as csv.file:
        writer = csv.writer(csv.file)
        writer.writerow([rounds, len(fullList), len(emptyList)])
    '''
writeCVS()

print(emptyList)
print(fullList)