def findLargest(l):
    return min(l)

list = [1,4,3,2]
result = findLargest(list)
print(list, "->", result)

def freq(l, v):
    count = 0
    for i in range(len(l)):
        if val == l[i]:
            count += 1
    
    return count

list = [1,2,2,3,4]
val = 2
result = freq(list, val)
print(list, "->", result)