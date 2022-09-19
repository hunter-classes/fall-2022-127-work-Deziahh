def bondify(name2): 
  result = ""
  spaceLocation2 = name2.find(" ")
  lastName2 = name2[spaceLocation2 + 1:].capitalize()
  statement = (lastName2 + ", " + name2.capitalize())
  result = statement
  return result

def piglatin(word):
  w = word[0]
  if w == "a" or "e" or "i" or "o" or "u":
    newWord = print(word + "yay")
    return newWord
  else:
    if w != "a" or "e" or "i" or "o" or "u":
      newWord = print(word[1:] + word[0] + "yay")
  return newWord

piglatin("apple")
piglatin("every")

piglatin("dog")

#Bondify Test
result = bondify("deziah gayle")
print("deziah gayle --> ",result)

#Piglatin Test
result = piglatin("apple")
print("apple --> ",result)
