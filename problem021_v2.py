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
    result_plus.append(sum(factor(number))
    
results = set()
for first, second in enumerate(result_plus):
    if size <= second:
        continue
    
    if first == second:
        continue
    
    if result_plus[second] == first:
        print(first, second)
        results.add(second)
        results.add(first)

answer = sum(results)