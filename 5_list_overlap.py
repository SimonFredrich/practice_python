import random

noCommonCount = 0
commonCount = 0

def list_overlap():

    global noCommonCount
    global commonCount

    a = []
    b = []

    count = 0

    while count < 10:
        count = count + 1
        a.append(random.randint(0, 61))
        b.append(random.randint(0, 61))    

    commonNumbers = []

    for i in a:
        if i in b:
            if i not in commonNumbers:
                commonNumbers.append(i)

    if not commonNumbers:
        noCommonCount += 1
    else:
        commonCount += 1


functionCount = 0

while functionCount < 1000:
    functionCount = functionCount + 1
    list_overlap()

print("Listen ohne Gemeinsamkeiten:", noCommonCount)
print("Listen mit Gemeinsamkeiten:", commonCount)