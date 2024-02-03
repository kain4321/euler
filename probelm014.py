def if_even(num):
    length = 1
    while num != 1:
        # print(num)
        if num % 2 == 0:
            num = num//2
            length += 1
        else:
            num = num*3 + 1
            length += 1
    return length

result2 = []
for i in range(1, 1000001):
    result = if_even(i)
    result2.append(result)
    
answer = max(result2)
true_answer = result2.index(answer) + 1
true_answer


numbers = [4, 8, 5, 13, 6, 2, 5, 18, 10, 13]
number_18_index = numbers.index(18)
print(number_18_index)