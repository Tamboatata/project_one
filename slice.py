'''
a [start:stop]  # beginnt bei Start und endet bei Stop -1
a [start:]      # beginnt bei Start und nimmt den Rest
a [:stop]       # beginnt bei null und endet bei Stop -1
a [:]           # kopiert den ganzen String

'''


string = "Teststring"

print(string[0:2]) #Te
print(string[2:4]) #Te

print(string[5:8]) #Te

print(string[2:]) #ststring
print(string[0:-1]) #Teststrin
print(string[0:-40]) #leerer String

print(string[1:500]) #eststring

string2 = string[:] #interessant, wenn man listen kopieren will (liste klonen)
print(string2)

input = "Ab--XYZ--89" # Übung

print(input[0:3]) #start stop
print(input[4:]) #start
print(input[:3]) #Stop
print(input[:])
print(input[-2::-5,-1])


# Länge einer Liste
a = [1,2,3]
print(len(a))

