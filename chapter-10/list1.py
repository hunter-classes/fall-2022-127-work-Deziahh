mylist = [76, 92.3, "hello", True, 4, 76]
print(mylist)

mylist.append("apple")
mylist.append(76)

mylist.insert(3, "cat")
mylist.insert(0, 99)

print(mylist)

print(mylist.index("hello"))
print(mylist.count(76))

mylist.remove(76)

mylist.pop(mylist.index(True))

print(mylist)
