a = "San Francisco ist schoen"
worte = a.split()
suchwort = "Francisco"

print(worte)
for wort in worte:
    if suchwort == wort:
        print("Suchwort {} gefunden".format(suchwort))
