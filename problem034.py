import math

num = math.factorial(10)

def separate(num):
    a = []
    while True:
        if num <= 0:
            break
        a.append(num % 10)
        num = int(num / 10)
    return a


def making_num():
    result = []
    for i in range(10, 10**7):
        x = 0
        a = separate(i)
        for digit in a:
            x += math.factorial(digit)
        if i == x:
            result.append(i)
    return result




w = making_num()
               


