#Getränkeauswahl

print("Getränke zur Auswahl: CocaCola, Pepsi Cola, Sprite")
Getränkeauswahl = input("Wählen Sie ihr Getränk aus: ")
print(Getränkeauswahl)

if Getränkeauswahl == "CocaCola":
    print("Sie haben eine CocaCola ausgewählt")
    print("CocaCola kostet 1.50 EUR")
    CocaCola = input("Bitte werfen Sie das Geld ein.")

elif Getränkeauswahl == "PepsiCola":
    print("Sie haben eine PepsiCola ausgewählt")
    print("PepsiCola kostet 2 EUR")
    PepsiCola = input("Bitte werfen Sie das Geld ein.")

elif Getränkeauswahl == "Sprite":
    print("Sie haben eine Sprite ausgewählt")
    print("Sprite kostet 2 EUR")
    Sprite = input("Bitte werfen Sie das Geld ein.")

else:
    print("keine Auswahl")
