def get_integer(prompt):
    return(int(input(prompt)))


def determinePrime(zahl):
    if zahl == 1:
        prime = False
    elif zahl == 2:
        prime = True
    else:
        prime = True
        for controlNumber in range(2, (zahl//2) + 1):
            if zahl%controlNumber == 0:
                prime = False
                break
    return prime

def printPrime(zahl):
    prime = determinePrime(zahl)
    if prime:
        descriptor = "eine"
    else:
        descriptor = "keine"
    print(zahl, " ist ", descriptor, " Primzahl.", sep="", end="\n\n")
                

while True:
    printPrime(get_integer("Gib eine Zahl ein: "))