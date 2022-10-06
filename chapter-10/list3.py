"""
5. Write a Python function named max that takes a parameter containing a nonempty list of integers and returns the maximum value.
(Note: there is a builtin function named max but pretend you cannot use it.)
"""
def max(list):
    num = 0
    for number in list:
        if number > num:
            num = number
    result = print(num)
    return result

numbers = [23, 45, 6]
max(numbers)

"""
7. Write a function to count how many odd numbers are in a list.
"""
def odd(list):
    odd_number = 0
    for item in list:
        if item%2 != 0:
            odd_number += 1
    result = print(odd_number)
    return result

list2 = [2,3,4,5]
odd(list2)

"""
8. Sum up all the even numbers in a list.
"""
def sum(list):
    sum = 0
    for n in list:
        if n%2 == 0:
            sum += n
    result = print(sum)
    return result

list3 = [2,3,8]
sum(list3)
    
