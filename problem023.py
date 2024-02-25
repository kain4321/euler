def factor(num):
    a = []
    for i in range(1,num + 1):
        if num % i == 0:
            a.append(i)
    a.remove(num)
    a = sum(a)
    return a

def finding(num1):
    a = [0]
    for i in range(1, num1 + 1):
        a.append(factor(i))
    return a

       
def factors_sum(num2):
    a = finding(num2)
    result = []
    for index, value in enumerate(a):
        if value > index:
            result.append(index)
    return result

numbers = factors_sum(30000)
numbers_sum = set()
for num1 in numbers:
    for num2 in numbers:
        numbers_sum.add(num1 + num2)
total_numbers = set(range(30000))
answer = total_numbers.difference(numbers_sum)