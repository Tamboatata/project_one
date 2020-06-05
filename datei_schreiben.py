from datetime import date

'''
'r'     This is the default mode. It Opens file for reading.
'w'     This Mode Opens file for writing.
        If file does not exist, it creates a new file.
        If file exists it truncates the file.
'a'     Open file in append mode.
        If file does not exist, it creates a new file.
'+'     This will open a file for reading and writing (updating)
'''
# open with File daten.txt and modus a+
file = open("daten.txt", "w+")

date_of_today = date.today().strftime("%m-%d-%Y")
file.write(date_of_today + "\r")

for i in range(10):
    file.write("This is line {0:d}\r".format(i + 1))

file.close()
