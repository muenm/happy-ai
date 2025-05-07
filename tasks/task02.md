# Aufgabe 2
a. Gebt den Python Code unten in euren Editor ein, klickt auf “Run” und beantwortet die Frage 
in der Konsole.

b. Lest euch den Quellcode und die Kommentare (mit # gekennzeichnet) durch.

c. Passt den Code so an, dass zu Beginn und nach 3 Sekunden immer ein neutraler Smiley 
angezeigt wird. 



```python 
def answer_question():
    # Aufforderung Eingabe zu machen
    eingabe = input("Schreib etwas: \n")

    # Wenn Eingabe nett ist --> lachender Smiley
    if eingabe == "Du bist toll":
        print(":-)")
    # Wenn die Eingabe gemein ist --> trauriger
    elif eingabe == "Du bist doof":
        print(":-(")

# Programm dauerhaft wiederholen
while True:
    answer_question()

```
