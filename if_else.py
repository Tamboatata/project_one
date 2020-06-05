import _random

# random library bietet Funktionen zum Erstellen von Zufallszahlen
# # https://docs.python.org/3/library/random.html

# zufallszahl zwischen 1 und 4. Dazu nutzen wir randint(1,4)
random_number = random.randint(1,4)

if random_number >= 4:
    print("die Zahl {} ist groesser oder gleich 4".format(random_number))
elif random_number >= 2:
    print("die Zahl {} ist groesser 1 und kleiner 4".format(random_number))
else:
    print("die Zahl {} ist kleiner als 2".format(random_number))


university = 8
experience = 1
python_experience = 4

if (university >= 4 and experience >= 2) or python_experience > 3.5:
    print("good programmer")