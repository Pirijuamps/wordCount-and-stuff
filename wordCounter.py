import json
with open("./abbreviations.json", 'r') as f:
    datastore = json.load(f)

myfile = open("./beatles.txt", "r")
data = myfile.read()
myfile.close()

words = data.lower().split()
muchWords = len(words)
print(data)
print("\nwow this much words: ", muchWords)

def specialCounter(specialWord, text):
    specialCounter = 0
    for x in text:
        if "'" in x:
            x = x.split("'")
            for y in x:
                if y == specialWord or y == datastore[specialWord]:
                    specialCounter+=1 
        elif x == specialWord:
            specialCounter+=1
    return specialCounter

specialWord = input()
print(specialWord, "appears a total of: ", specialCounter(specialWord, words))