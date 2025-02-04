import random
#Variablen definieren
num = random.randint(1,10)
#Maximale Versuche
guess_max = 10
#Gemachte Versuche
guess_count = 0
#List geratene Zahlen
guesses = []

def ausgabe(text):
    print(text)
    print("du hast " + str(len(guesses)) + " versuche gebraucht")
    for g in guesses:
        print(g)

#Vergleich Input mit Num bis erfolgreich oder guess_max erreicht
while guess_count < guess_max:
    #Input User
    guess = int(input("Rate die Zahl?"))  
    guesses.append(guess)
    #wenn gesucht höher dann higher
    if guess < num:
        print("Die gesuchte Zahl ist höher.")
        guess_count += 1
    #Wenn gesucht niedriger dann lower
    elif guess > num:
        print("Die gesuchte Zahl ist niedriger.")
        guess_count += 1
    #Wenn gleich dann gewonnen
    else:
        # print("Du hast gewonnen!" + str(guesses))
        ausgabe("du hast gewonnen")
        break

if guess_count == guess_max:
    # print("Du hast verloren." + str(guesses))
    ausgabe("du hast verloren")
    