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