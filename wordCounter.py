myfile = open("wordCounter/beatles.txt", "r")
data = myfile.read()
myfile.close()

words = data.split(" ")
muchWords = len(words)
print(data)
print("\nwow this much words: ", muchWords)

