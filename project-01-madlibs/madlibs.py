import random

names = ["Deziah", "Andrea", "Ally", "Sam"]
schools = ["Hunter", "MHC", "CCNY", "Baruch"]
majors = ["CompSci", "English", "Math"]
verbs = ["destroyed", "earned", "accepted", "offer", "behaved"]
nouns = ["dog", "hammer", "cat", "car"]


# Open the Mad Libs text file
f = open("madlibs.txt")
 
# Read the whole file and store each line in a list
madlibText = f.readlines()
 
# Choose a random line from the list
madlib = random.choice(madlibText)


madlib = madlib.replace("blankName", random.choice(names))
madlib = madlib.replace("blankSchool", random.choice(schools))
madlib = madlib.replace("blankMajor", random.choice(majors))
 
# Print out the Mad Lib including the user's response
print(madlib)

