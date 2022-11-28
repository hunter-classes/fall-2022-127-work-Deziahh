#Stored my translations in a file named pirate.dat

pirateWords = {}
l = []

pirateKeys = list(pirateWords.keys())
pirateValues = list(pirateWords.values())

dictFile = open("pirate.dat")
dictFileData = dictFile.read()
dictFileData = dictFileData.split("\n")

for word in dictFileData:
    findColon = word.find(":")
    colon = word[findColon + 1:]
    l1 = l.append(colon)

pirateWords["hi"] = l[0]
pirateWords["buddy"] = l[1]
pirateWords["earlier"] = l[2]
pirateWords["guys"] = l[3]

textFile = open("input.txt")
textFileData = textFile.read()
textFileData = textFileData.split("\n")

pirateKeys = list(pirateWords.keys())
pirateValues = list(pirateWords.values())

textFileData = [line.replace(pirateKeys[0], pirateValues[0]) for line in textFileData]
textFileData = [line.replace(pirateKeys[1], pirateValues[1]) for line in textFileData]
textFileData = [line.replace(pirateKeys[2], pirateValues[2]) for line in textFileData]
textFileData = [line.replace(pirateKeys[3], pirateValues[3]) for line in textFileData]

done = " ".join(textFileData)
print(done)

textFile.close()
dictFile.close()