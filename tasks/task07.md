# Aufgabe 7

a. Nutzt die Confidence des maschinellen Lernmodells in Python. Speichert die Confidence in einer Variable (Zeile 25). Die Confidence wird in Prozent angegeben und ist ein Maß für die Sicherheit der Entscheidung. Z.B. kann sich euer Charakter zu x% sicher sein, dass die Eingabe “Du bist toll” nett ist. 

b. Lasst euren Charakter in Abhängigkeit davon reagieren, wie sicher er / sie sich ist. Wenn sich euer Charakter einigermaßen sicher ist, soll wie zuvor ein lachender oder trauriger Smiley angezeigt werden. Ansonsten soll der Charakter sagen: “Ich verstehe dich nicht…”. 

c. Gebt den Code unten in euren Editor ein. Klickt auf “Run” (Play Symbol) und schaut euch das Ergebnis in der Konsole an.

d. Überlegt, wie ihr euer Programm erweitern könntet. 

```python
import time
import requests

# Diese Funktion übergibt euren Text an die KI
# und gibt die Kategorie mit der höchsten Wahrscheinlichkeit zurück
def classify(text):
    key = "HIER API KEY REIN"
    url = "https://machinelearningforkids.co.uk/api/scratch/"+ key + "/classify"

    response = requests.get(url, params={ "data" : text})

    if response.ok:
        responseData = response.json()
        topMatch = responseData[0]
        return topMatch
    else:
        response.raise_for_status()

def answer_question():
    # Aufforderung Eingabe zu machen
    eingabe = input("Schreib etwas: \n")
    klassifikation = classify(eingabe)
    kategorie = klassifikation["class_name"]

    # Speichert die Confidence in einer Variable 
    # Passt den Code hier so an, dass die Confidence berücksichtigt wird:
    # Wenn sich euer Charakter sicher ist (was bedeudet das????)
    # Dann soll es eine Antwort geben, sonst soll die Ausgabe kommen "ich verstehe dich nicht"

    # Wenn Eingabe nett ist --> lachender Smiley
    if kategorie == "Nett":
        print(":-)")
    # Wenn die Eingabe gemein ist --> trauriger
    elif kategorie == "Gemein":
        print(":-(")
    else:
        print("Keine Klassifikation möglich \n")

    time.sleep(3)
    print(":-|")

# Bei Programmstart neutrales Smiley
print(":-|")

# Programm dauerhaft wiederholen
while True:
    answer_question()
```