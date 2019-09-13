myfile = open("wordCounter/beatles.txt", "r")
data = myfile.read()
myfile.close()

words = data.split(" ")
muchWords = len(words)
print(data)
print("\nwow this much words: ", muchWords)



def specialCounter(specialWord, text):
    specialCounter = 0
    for x in text:
        if x.__contains__("'"):
            x.split("'")
    return specialCounter

specialWord = input()
print(specialWord, "appears a total of: ", specialCounter(specialWord, words))