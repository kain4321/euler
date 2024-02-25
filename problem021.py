def factor(num):
    a = []
    for i in range(1,num + 1):
        if num % i == 0:
            a.append(i)
    a.remove(num)
    return a

size = 301
result = [[]]
result_plus = [0]
for number in range(1, size):
    result.append(factor(number))
    result_plus.append(sum(factor(number)))

amicables = set()
for index, number in enumerate(result_plus):
    if index == number:
        continue
    if size <= number:
        continue
    if result_plus[number] == index:
        print(index, number)
        amicables.add(index)
        amicables.add(number)

answer = sum(amicables)