# Getränkeauswahl
# Getränkeautomat
from random import choice

print("Getränke zur Auswahl: CocaCola, Pepsi Cola, Sprite")
getränkeauswahl = input("Wählen sie ihr Getränk aus. ")

if getränkeauswahl == "CocaCola":
    print("Sie haben eine CocaCola gewählt")
    print("CocaCola kostet 1.50 EUR")
    preis = 150

elif getränkeauswahl == "PepsiCola":
    print("Sie haben eine Pepsi Cola gewählt")
    print("PepsiCola kostet 2.00 EUR")

    preis = 200


elif getränkeauswahl == "Sprite":
    print("Sie haben eine Sprite gewählt")
    print("Sprite kostet 2.00 EUR")

    preis = 200

else:
    print("Sie haben kein passendes Getränk gewählt. ")
    getränkeauswahl = input("Wählen sie ihr Getränk aus. ")

coins = input("Bitte werfen Sie {} Münzen ein".format(preis)).split()

coins = coins[:3]

total_sum = 0
count = 0
for coin in coins:
    if coin == "50" or "100" or "200":
        if coin == "100":
            coin = choice([0, 100])
            coin = int(coin)
            total_sum += coin
            if coin == 100:
                count += 1
        else:
            coin = int(coin)
            total_sum += coin
            count += 1

if total_sum >= preis:
    change = total_sum - preis
    print("Bestellung erfolgreich. Sie haben {} bestellt. {} Münzen eingeworfen. Ihr Wechselgeld beträgt {} Cent)"\
          .format(getränkeauswahl,count, change))
else:
    print("Nicht genug Guthaben. Bitte werfen Sie erneut Münzen ein.")

coins = input("Bitte werfen Sie {} Münzen ein".format(preis)).split()

coins = coins[:3]

for coin in coins:
    if coin == "50" or "100" or "200":
        if coin == "100":
            coin = choice([0, 100])
            coin = int(coin)
            total_sum += coin
            if coin == 100:
                count += 1
        else:
            coin = int(coin)
            total_sum += coin
            count += 1


if total_sum >= preis:
    change = total_sum - preis
    print("Bestellung erfolgreich. Sie haben {} bestellt. {} Münzen eingeworfen. Ihr Wechselgeld beträgt {} Cent)" \
          .format(getränkeauswahl, count, change))