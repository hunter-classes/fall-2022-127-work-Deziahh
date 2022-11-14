pirateWords = {"Hello":"Ahoy",
               "buddy":"matey"}

pirateKeys = list(pirateWords.keys())
pirateValues = list(pirateWords.values())


file = open("input.txt")
fileData = file.read()
fileLines = fileData.split("\n")

#print(list(pirateWords.keys())[0])

fileLines = [line.replace(pirateKeys[0], pirateValues[0]) for line in fileLines]
fileLines = [line.replace(pirateKeys[1], pirateValues[1]) for line in fileLines]


done = " ".join(fileLines)
print(done)