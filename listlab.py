"""
1. Write a function to find the smallest value in a listKfind smallest in a list of items
"""
def findSmallest(l):
    list2 = min(l)
    
    return list2

#Test
list = [1,2,3,4,5]
result = findSmallest(list)
print("#1. ",list, "->", result)
    
"""
2. Write a function that returns a new list that contains all the odd items in the original list
"""
def newList(list):
    secondList = []
    for odd in list:
        if odd%2 != 0:
            secondList.append(odd)
    return secondList

#Test
list1 = [1,2,3,4,5]
result = newList(list1)
print("#2. ",list1, "->",result)

"""
3. Write a function that takes a string and returns a new string where all the words are capitalized.
"""
def capitalize_each_word(original_str):
    result = ""
    list_of_words = original_str.split()
    for word in list_of_words:
        if len(result) > 0:
            result = result + " " + word.strip().capitalize()
        else:
            result = word.capitalize()
    if not result:
        return original_str
    else:
        return result
    
sample = "oh happy day"
result = capitalize_each_word(sample)
print("#3. ",sample, "->",result)
"""
4. Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case
"""
def fiveString(string):
    secondString = " "
    sString = string.split()
    for word in sString:
        if len(word) > 5:
            newWord = word.upper()
            secondString += " " + newWord
            
    return secondString
    
ss = "theres the theirs"
result = fiveString(ss)
print("#4. ",ss,"->",result)
"""
5. Write a function that takes a list of numbers and returns a new list with each item squared
"""
def squared(list):
    finalList = []
    for i in list:
        finalList.append(i ** 2)
    
    return finalList

sq = [2,3,4]
result = squared(sq)
print("#5. ", sq, "->", result)
"""
6. Write a function that takes two lists of numbers and returns a new list where each item is the corresponding values of the original
lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
"""
def addLists(list1, list2):
    l3 = []
    for i in range(len(list1)):
        ab = list1[i] + list2[i]
        l3.append(ab)
    
    return l3

l1 = [1,2,3]
l2 = [1,2,3]
result = addLists(l1, l2)
print("#6. ",l1, l2, "->", result)
"""
7. chapter 10 # 10: Count how many words in a list have length 5.
"""
def count(string):
    word_count = 0
    seperate = string.split()
    for word in seperate:
        if len(word) == 5:
            word_count += 1
    
    return word_count

s = "My name is Deziah. There are no words there."
s2 = "Happy Day Love Juice Nasty"
result = count(s2)
print("#7. ", s2, "->", result)
"""
8. chapter 10 #11: Sum all the elements in a list up to but not including the first even number.
"""       
"""
9. chapter 10 #12: Count how many words occur in a list up to and including the first occurrence of the word “sam”.
"""
def samCount(list):
    keyWord = "sam"
    keyWord2 = "Sam"
    count = 0
    for i in list:
        count += 1
        if i == keyWord or i == keyWord2:
            break
    
    return count

words = ["savior", "sound", "song","Sam","song"]
result = samCount(words)
print("#9. ", words, "->", result)