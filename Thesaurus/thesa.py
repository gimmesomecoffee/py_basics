import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif len(get_close_matches(w, data.keys())) > 0:
        yn = input("Did u mean %s instead? Enter Y if yes, or N if no. " % get_close_matches(w, data.keys())[0])
        yn = yn.upper()
        if yn == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif yn == "N":
            return "The word doesn't exists, please double check"
        else:
            return "We didn't understand your entry"
    else:
        return "didnt find"
    


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
        for item in output:
             print(item)
else:
     print(output)





