def findLargest(l):
    return min(l)

list = [1,4,3,2]
result = findLargest(list)
print(list, "->", result)

def freq(list, v):
    count = 0
    for i in list:
        if i == v:
            count += 1
    
    return count

list = [1,2,2,3,4]
result = freq(list, 2)
print(list, "->", result)