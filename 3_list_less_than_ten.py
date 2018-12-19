number_by_user = int(input("Bitte gib eine Zahl an: "))
the_list = range(1000)

other_list = []
for element in the_list:
    if element < number_by_user:
        other_list.append(element)

print("Zahlen die niedriger als die angegebene Zahl sind:", other_list)

