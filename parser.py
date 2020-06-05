file = open("trump_speeches.txt", "r")

# Liste mit Sätzen erstellen
sentences = file.read()[0:500].split(".")

modus = input("\nWähle einen Modus aus! Modi: SEN / WORD / TOP \n")
if modus != "TOP":
    suchwort = input("Bitte Suchwort eingeben\n")
result = []
result_words = []

for sentence in sentences:
    if len(sentence) > 3:
        sentence = sentence.strip()
        if suchwort in sentence:
            print(sentence)
            result.append(sentence)
            result += sentence.split()
    else:
        sentences.remove(sentence)

if modus == "SEN":
    print(result)

elif modus == "WORD":
    for word in result:
        if suchwort in word:
            if suchwort not in result_words:
                result_words.append(word)
print(result_words)





#if modus == "SEN":
#elif modus == "WORD":

