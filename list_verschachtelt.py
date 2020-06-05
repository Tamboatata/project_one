names = [
    ["Andi", "Kolb"],
    ["Peter", "Meier"],
    ["Andreas", "Walter"],
    ["Sandra", "Schneider"]
]
def sort_nachname(n):
    '''Parameter [vorname, nachname]'''
    return n[1]

# nach nachnamen sortiert
names.sort(key=sort_nachname, reverse=True)
print(names)

