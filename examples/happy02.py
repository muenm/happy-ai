import time

def answer_question():
    # Aufforderung Eingabe zu machen
    eingabe = input("Schreib etwas: \n")

    # Wenn Eingabe nett ist --> lachender Smiley
    if eingabe == "Du bist toll":
        print(":-)")
    # Wenn die Eingabe gemein ist --> trauriger
    elif eingabe == "Du bist doof":
        print(":-(")

    time.sleep(3)
    print(":-|")

# Bei Programmstart neutrales Smiley
print(":-|")

# Programm dauerhaft wiederholen
while True:
    answer_question()