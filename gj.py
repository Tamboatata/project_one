names = [
    ["Andi", "Kolb"],
    ["Peter", "Meier"],
    ["Andreas", "Walter"],
    ["Sandra", "Schneider"]
]

names.sort()


def sort_nachname(n):
    ''' Parameter [vorname, nachname]'''


return n[1]

# nach nachnamen sortiert lambda
names.sort(key=sort_nachname, reverse=True)
print(names)
