import json

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    else:
        return "didnt find"
    

while True:
    word = input("Enter a word: ")
    
    print(translate(word))
    





