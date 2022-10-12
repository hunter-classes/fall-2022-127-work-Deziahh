"""
1. Write a function to find the smallest value in a listKfind smallest in a list of items
"""
def findSmallest(list):
    list2 = min(list)
    result = print(list2)
    return result

list0 = [1,2,3,4,5]
findSmallest(list0)
    
"""
2. Write a function that returns a new list that contains all the odd items in the original list
"""
def newList(list):
    secondList = []
    for odd in list:
        if odd%2 != 0:
            secondList.append(odd)
    result = print(secondList)
    return result

list1 = [1,2,3,4,5]
newList(list1)

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
print(result)
"""
4. Write a function that takes a string and returns a new string with every word that's longer than 5 character turned into upper case
"""
"""
5. Write a function that takes a list of numbers and returns a new list with each item squared
"""
def squared(list):
    finalList = []
    for i in list:
        finalList.append(i ** 2)
    result = print(finalList)
    return result

sq = [2,3,4]
squared(sq)
"""
6. Write a function that takes two lists of numbers and returns a new list where each item is the corresponding values of the original
lists added together. Ex [1,2,3] and [10,20,30] would return the list [11,22,33]
"""
def addLists(list1, list2):
    l3 = []
    for i in range(len(list1)):
        ab = list1[i] + list2[i]
        l3.append(ab)
    result = print(l3)
    return result

l1 = [1,2,3]
l2 = [1,2,3]
addLists(l1, l2)
"""
7. chapter 10 # 10: Count how many words in a list have length 5.
"""
def count(string):
    word_count = 0
    seperate = string.split()
    for word in seperate:
        if len(word) == 5:
            word_count += 1
    result = print(word_count)
    return result

s = "My name is Deziah. There are no words there."
s2 = "Happy Day Love Juice Nasty"
count(s)
count(s2)
"""
8. chapter 10 #11: Sum all the elements in a list up to but not including the first even number.
"""       
"""
9. chapter 10 #12: Count how many words occur in a list up to and including the first occurrence of the word “sam”.
"""
def samCount(list):
    keyWord = "sam"
    count = 0
    for i in list:
        count += 1
        if i == keyWord:
            break
    result = print(count)
    return result

words = ["savior", "sound", "song","sam","song"]
samCount(words)