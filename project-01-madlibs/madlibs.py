#Extra 1: I wrote a story in another file and read it in my program
#Extra 2: Unique replacement (heroName)

import random

names = ["Deziah", "Andrea", "Ally", "Sam", "David", "Max"]
rooms = ["living rooom", "bedroom", "dining room"]
adjectives = ["silly", "enormous", "fun","fantastic"]
verbs = ["destroyed", "earned", "accepted", "offer", "behaved"]
adverbs = ["slowly", "yesterday", "today", "rarely"]
nouns = ["dog", "hammer", "cat", "car"]
animals = ["puppy", "kitten", "mouse"]
food = ["pizza", "cheeseburgers", "salmon", "rice", "chicken"]

randomName = random.choice(names)
names.remove(randomName)

# Open the Mad Libs text file
f = open("madlibs.txt")
 
# Read the whole file and store each line in a list
madlibText = f.read()
madlibList = madlibText.split("\n")


madlibList = [sentence.replace("heroName", randomName) for sentence in madlibList]

madlibList = [sentence.replace("blankName", random.choice(names)) for sentence in madlibList]
madlibList = [sentence.replace("blankRoom", random.choice(rooms)) for sentence in madlibList]
madlibList = [sentence.replace("blankAdjective", random.choice(adjectives)) for sentence in madlibList]
madlibList = [sentence.replace("blankVerb", random.choice(verbs)) for sentence in madlibList]
madlibList = [sentence.replace("blankAdverb", random.choice(adverbs)) for sentence in madlibList]
madlibList = [sentence.replace("blankNoun", random.choice(nouns)) for sentence in madlibList]
madlibList = [sentence.replace("blankAnimal", random.choice(animals)) for sentence in madlibList]
madlibList = [sentence.replace("blankFood", random.choice(food)) for sentence in madlibList]

x = " ".join(madlibList)
print(x)

f.close()