
fruits = ["apple", "banana","cherry"]
frutti = fruits

print(fruits[0][1])
print(fruits[0])

print("Länge der Liste: ", len(fruits))

#Index in der Liste ist apple=0 banana = 1 cherry = 3

#Datentyp von List-Element an Index 0
fruit = fruits[0]
print(type(fruit))

#index von Wert zurückgeben lassen
print(fruits.index("banana"))

a = "Teststring"
print(a[0])
# a[0]="P" das geht nicht, weil Strings sind unveränderlich

# ich kann aber den Index 0 Verändern von Apple zu Strawberry.\
# Listen sind im Vergleich zu Strings veränderlich
fruits[0] = "Strawberry"
print(fruits)

# neues Element einfügen
fruits.insert(1, "lemon")
print(fruits)
print(fruits.index("banana"))

# neues Element der Liste hinzufügen
fruits.append("pineapple")
print(fruits)

#Mehrere Elemente an Liste anhängen
# fruits = fruits ["coconut", "strawberry", "apple"]
fruits+= ["coconut", "strawberry", "apple", "apple"]
# alternative Möglichkeit
fruits.extend(["Orange", "Quitte"])
print(fruits)

# Prüfen ob Element in der Liste ist
if "apple" in fruits:
    print("jo, der Apfel ist hier drin")

# Elemente aus der Liste herauslöschen
fruits.remove("apple")
fruits.remove("apple")

# Das Listenelement in Position 0 wird entfernt --> Strawberry
del fruits[0]
print(fruits)

# Liste einfach nur leeren
#fruits.clear()
print(fruits)

# Löscht nicht nur den Inhalt, sondern die ganze Liste
#del fruits

# Stapelspeicher --> last in first out
print(fruits)
s = fruits.pop()
print(s)
print(fruits)
#frutti ist gleich fruits deshalb verändert sich liste mit. Fruits und Frutti sind nur referenzen. wenn sich etwas in der Liste verändert, verändert sich nicht die referenz
print(frutti)

# aus leerer Liste pop aufrufen
#[].pop()
#print()






