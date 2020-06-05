# Hier wurde eine Funktion eingefügt

# per reference --> es wurde für p das Element "Apple" hinzugefügt in dem auf liste referriert wurde
def check_list(liste):
    liste.append("apple")

fruits = ["birne", "cherry", "birne", ["birne"]]
new_fruits = fruits[:] #hier ist es anders als frutti und fruits aus liste.py weil hier eine neue Liste erstellt wird
# für index 0 wird pinapple der liste von fruits hinzugefügt
fruits[0] = "Pineapple"
#print(id(p[0]))
#print(id(p[2]))
#print(id(p[1]))
#print(id(p[3][0]))

print(fruits)
print(new_fruits)

