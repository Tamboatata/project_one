'''
Das Programm soll Grad Celcius durch Usereingabe in Fahrenheit umrechnen
'''
celcius = None
fahrenheit = None
celcius = float(input("Temperature in Grad Celcius"))  # type: float


fahrenheit = celcius * 1.8 + 32

print(fahrenheit)

msg = "Grad sind %0.2f Fahrenheit" % celcius, fahrenheit
print(msg)