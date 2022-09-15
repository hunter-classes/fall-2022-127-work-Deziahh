def is_even(n):
    if n % 2 == 0:
        result = True
    else:
        result = False
        
    return result

def is_odd(n):
    if n % 2 > 0:
        result = True
    else:
        result = False
        
    return result
  
def is_rightangled(a,b,c):
    if abs(c**2 - (a**2 + b**2) < 0.001):
        result = True
    else:
           result = False
    return result

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

def is_rightangled_two(a, b, c):
    is_rightangled_two = False

    if a > b and a > c and abs(b**2 + c**2 - a**2) < 0.001:
        result = True
    elif b > a and b > c and abs(a**2 + c**2 - b**2) < 0.001:
        result = True
    elif c > a and c > b and abs(a**2 + c**2 - b**2) < 0.001:
        result = True
    else:
        result = False
    return result

a = float(input("Side 1: "))
b = float(input("Side 2: "))
c = float(input("Side 3: "))

#statements
print(is_even(2))
print(is_odd(9))
print(is_rightangled(a,b,c))
print(is_rightangled_two(a,b,c))
