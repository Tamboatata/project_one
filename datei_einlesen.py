'''
'r' This is the default mode. It Opens file for reading.
'w' This Mode Opens file for writing.
If file does not exist, it creates a new file.
If file exists it truncates the file.
'a' Open file in append mode.
If file does not exist, it creates a new file.
'+' This will open a file for reading and writing (updating)
'''

file = open("daten.txt", "r")
content = file.read()
print(content)

lines = file.readlines()


for line in lines:
    print(line.rstrip('\n'))
