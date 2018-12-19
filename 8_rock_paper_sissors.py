user1 = input("Name des 1. Spielers: ")
user2 = input("Name des 2. Spielers: ")
user1_answer = input(user1 + ", wähle Stein, Schere oder Papier: ")
user2_answer = input(user2 + ", wähle Stein, Schere oder Papier: ")

def compare(u1, u2):
    if u1 == u2:
        return("Unentschieden!")
    elif u1 == "stein":
        if u2 == "schere":
            return(user1 + " hat mit Stein gewonnen!")
        else:
            return(user2 + " hat mit Papier gewonnen!")
    elif u1 == "schere":
        if u2 == "papier":
            return(user1 + " hat mit Schere gewonnen!")
        else:
            return(user2 + " hat mit Stein gewonnen!")
    elif u1 == "papier":
        if u2 == "stein":
            return(user1 + " hat mit Papier gewonnen!")
        else:
            return(user2 + " hat mit Schere gewonnen!")
    else:
        return("Du hast etwas falsches eingegeben! Versuche es nochmal.")
    
print(compare(user1_answer.lower(), user2_answer.lower()))