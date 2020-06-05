a = True

if a:
    print("a ist wahr")
else:
    print("a ist nicht wahr")

b = False
if not b:
    print("b ist nicht wahr")

ages = [12,14,15,34]

if 12 in ages:
    print("ja, 12 ist in der Liste enthalten")


parents = 20
children = 10
#Wenn es mehr als 20 Personen sind dann mach irgendwas
if parents + children > 25:
    print("zu viele Personen")

country = input("Aus welchem Land kommst du?")

if country == "Frankreich" or country == "frankreich":
    print("Die Person kommt aus Frankreich")
elif country == "Deutschland":
    print("Die Person kommt aus Deutschland")
else:
    print("Das Land {} ist leider unbekannt".format(country))
