import random

numberList = []
listLenght = random.randint(10, 20)

while len(numberList) < listLenght:
    numberList.append(random.randint(1,71))

numberList.sort()

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
evenNumbers = [item for item in numberList if item%2 == 0]

evenNumbers.sort()

print(numberList)
print(evenNumbers)