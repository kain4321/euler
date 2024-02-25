
def every(num):
    a = [0]
    b = a[1:] +num[2]+ a[:0]
    return b


result = [[]]
numbers = list(range(10))
for num in numbers:
    new_result = []
    for prefix in result:
        for i in range(len(prefix) + 1):
            new_result.append(prefix[:i] + [num] + prefix[i:])
    result = new_result

result.sort()
result[10**6-1]


from itertools import permutations

numbers = list(range(10))
result = list(permutations(numbers))
result[10**6-1]
