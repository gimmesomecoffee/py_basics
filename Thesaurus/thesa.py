import json

data = json.load(open("data.json"))

def translate(w):
    if w in data:
        return data[w]
    else:
        return "didnt find"
    

while True:
    word = input("Enter a word: ")
    
    print(translate(word))
    




