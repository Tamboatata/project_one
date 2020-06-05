b = "San Francisco"
# Länge eines Strings mit einer build-in len Funktion
print(len(b))

#Länge einer Liste
a = [1, 3, 4]
print(len(a))

# Methoden sind objektfunktionen --> mit der String METHODE (=Objekt-Funktion) split() String in Sub-Strings zerlegen
b.split()

city = "Sommer in New York.City"
res = city.split()
print(res)
# default Trenner von Split ist der Whitespace (leerzeichen)

# eigenes Trennzeichen übergeben
res = city.split(".")
res = res[0].split()
print(res)

print(res[1:3])
