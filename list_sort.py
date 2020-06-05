names = ["Peter", "Bernd", "Martin"]
print(names)

# Liste sortieren: Aufsteigend ab A
names.sort()
print(names)
# Liste sortieren: Absteigend ab Z
names.sort(reverse=True)
print(names)

# Zahlen sortieren aufsteigend
numbers = [1,7,3,7]
numbers.sort()
print(numbers)

# Zahlen (auch floats) sortieren absteigend
numbers = [0.9, 0.1, 0.5]
numbers.sort(reverse=True)
print(numbers)
# gemischtartige Listen wie list[0.9, New York, 1] kann man nicht sortieren

