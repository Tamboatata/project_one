# coding=utf-8
# 1.1 Addition
a = 2
b = 2.3
c = a + b
d = b + a + b
print(type(c))
print(c)
print(type(d))
print(d)

# 1.2 Addition
a = 12.3
b = 3553
c = a + b
print(type(c))
print(c)


# 1.3 Division
a = 12.3
b = 3553
c = a / b
d = (a / b) / a
print(type(c))
print(c)
print(type(d))
print(d)

# 1.4 Division und 1.5 Division
a = 1
b = 0.1
c = a / b
d = (b / a)
print(type(c))
print(c)
print(type (d))
print(d)

# 1.6 Division
a = 1
b = 0
try:
    c = a / b
    print(type(c),"c=", c)
except ZeroDivisionError:
    print('Bei der Berechnung von d wird durch null geteilt')
try:
    d = (b / a)
    print(type(d),"d=", d)
except:
    print("Div0")
print("")

# 1.7 Subtraktion
a = 12.3
b = 12
c = a - b
d = b - a
print(type(c))
print(c)
print(type(d))
print(d)

#1.8 Multiplikation
a = 12.3
b = -12
c = a * b
d = b * a
print(type(c))
print(c)
print(type(d))
print(d)

#1.9 Multiplikation
a = 0.0
b = 0
c = a * b
d = b * a
print(type(c))
print(c)
print(type(d))
print(d)

#1.10 Exponent
a = 2
b = 4
c = b ** a
d = a ** b
print(type(c))
print(c)
print(type(d))
print(d)

#1.11 Exponent
a = 0
b = 2
c = a ^ b
d = b ^ a
print(type(c))
print(c)
print(type(d))
print(d)

# Rechnen mit Rest (Modulo) (Modul ist % in Python
a = 43
b = 3
c = a % b

print(type(c))
print(c)

# 2 Exponentiation
a = 2
for b in range(0, 5):
    d = a ** b
    print(type(d), "d=", d, " - bei b= ", b)
print("")

# 3 User Eingabe '''Schreibe ein Programm, welches eine Zahl (inch) als User Input entgegennimmt (input) in Zentimeter umrechnet
# Ein Inch entsprechen 2,54 Zentimeter - Formatiere die Ausgabe mit Print und Format
Inch = None
Zentimeter = None
Inch = float(input("Inch in Zentimeter"))

Zentimeter = Inch * 2.54
print(Zentimeter)
msg = "Inch sind %0.2f Zentimeter" % Inch, Zentimeter
print(msg)

# 4 Abrunden
number_1 = round(3.234)
print(number_1)
number_2 = round(4.43)
print(number_2)
number_3 = round(12233.3)
print(number_3)

# 5 Schreibe ein Programm, welches Grad in Bogenmaß umrechnet
import math
input = 360
math.radians(input)
b = math.radians(input)
print(b)





