
import random

names = ["Deziah", "Andrea", "Ally", "Sam"]
rooms = ["living rooom", "bedroom", "dining room"]
adjectives = ["silly", "enormous", "fun","fantastic"]
verbs = ["destroyed", "earned", "accepted", "offer", "behaved"]
adverbs = ["slowly", "yesterday", "today", "rarely"]
nouns = ["dog", "hammer", "cat", "car"]
animals = ["puppy", "kitten", "mouse"]
food = ["pizza", "cheeseburgers", "salmon"]


# Open the Mad Libs text file
f = open("madlibs.txt")
 
# Read the whole file and store each line in a list
madlibText = f.read()
madlibList = madlibText.split("\n")

madlibList = [s.replace("blankName", random.choice(names)) for s in madlibList]
madlibList = [s.replace("blankRoom", random.choice(rooms)) for s in madlibList]
madlibList = [s.replace("blankAdjective", random.choice(adjectives)) for s in madlibList]
madlibList = [s.replace("blankVerb", random.choice(verbs)) for s in madlibList]
madlibList = [s.replace("blankAdverb", random.choice(adverbs)) for s in madlibList]
madlibList = [s.replace("blankNoun", random.choice(nouns)) for s in madlibList]
madlibList = [s.replace("blankAnimal", random.choice(animals)) for s in madlibList]
madlibList = [s.replace("blankFood", random.choice(food)) for s in madlibList]

print(madlibList)