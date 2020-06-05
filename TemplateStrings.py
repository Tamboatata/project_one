#String-Methode format()

string1 = "Das ist ein Template {}".format("String")
#wenn neben {} noch ein {} eingefügt wird, kommt fehlermeldung, weil ein Platzhalter leer ist
print(string1)

# Template String mit zwei Platzhaltern
string2 = "Es sind viele {} {}".format("natürlich", "möglich")
print(string2)

# übergebene Werte können auch Zahlen sein --> Platzhalter waren implizit
string1 = "a:{}, b:{}, c:{}".format(2, 4, 9)
print(string1)

# Platzhalter sind explizit

string1 = "a:{2}, b:{0}, c:{1}".format(2, 4, 9)
print(string1)

# Beispiel mit Namen
user = "Vorname: {1} Nachname: {0}, Stadt: {2}".\
    format("Otto", "Totto", "Berlin")
print(user)

# Beispiel mit Bruch
string1 = "a:{0}, b:{1}, c:{2}".format(2, 4, 1/3)
print(string1)

# formatieren mit Format
string1 = "a:{0:d}, b:{1}, c:{2:0.2f}".format(20000, 34, 1/3)
print(string1)

# gleichen Wert in Platzhalter mit selbem Indes schreiben
string1 = "precisions: {0:0.1f} or {0:0.3f}".format(331.4148)
print(string1)

coords = "Coordinates: {latitude}, {longitude}".\
    format(latitude='37,24N', longitude='-115.81W')
print(coords)