# das ist ein String
string = "eggs"
print(id(string))
#Strings nicht unveränderbar, d. h hier gibt es einen Fehler, wenn einkommentiert
#string[0]="A" --> nicht möglich

# das letzte Zeichen im String mit negativen Wert beginnt Zählung von hinten
print(string[-1])

# leerer String
string = "" # if string: falsch

print(id(string))

string = 3 * "XXX-"
print(string)

string = "eggs"
string2 = "spam"
string3 = "spam"
# string3 == string2 ergibt boolgschen Wert True
if string3 == string2:
    print(id(string2))
    print(id(string3))
    print("Strings 3 und 2 sind gleich")

if string == string2:
    print("Strings sind gleich")
if string3 == string2:
    print("Strings 2 und 3 sind gleich")

if "eg" in string:
    print("in diesem String ist ein kleines eg vorhanden")