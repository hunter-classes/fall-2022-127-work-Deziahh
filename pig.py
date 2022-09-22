def piglatin(word):
  w = word[0]
  #wc = word.capitalize()
  if w in "aeiou":
    result = word + "yay"
  else:
    result = word[1:] + word[0] + "yay"
    
  return result

#Piglatin Test
result = piglatin("apple")
print("apple --> ",result)

result = piglatin("dog")
print("dog --> ",result)