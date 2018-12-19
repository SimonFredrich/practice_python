from datetime import date

name = input("Gib deinen Namen ein: ")
age = int(input("Gib dein alter ein: "))

today = date.today()

years_to_hundred = 100 - age
final_year = str(today.year + years_to_hundred)

message = "Im Jahre " + final_year + " wird " + name + " Hundert Jahre alt sein.\n"
print(message)

copy_number = int(input("Wie viele Kopien von diesem Satz? "))

print(copy_number * message)