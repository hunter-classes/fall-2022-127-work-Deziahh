def average(numbers):
  avg = 0
  for num in numbers:
      avg = avg + num
  print(avg / len(numbers))

#test:
numbers = [4, 3, 3, 5]
average(numbers)

list = [2,3,4]
def sum_of_squares(list):
    sumSquares = 0
    for number in list:
        sumSquares += number ** 2
    return sumSquares
#test:
print(sum_of_squares(list))
