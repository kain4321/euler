from itertools import permutations

def make_num(a):
    string = ''
    for i in a:
        string += str(i)
    result = int(string)
    return result

numbers = list(range(1, 10))
result = list(permutations(numbers))

answer = set()
count = 1
while count != 362880:
    n = result[count]
    a = make_num(n[:3])
    b = make_num(n[3:5])
    c = make_num(n[5:])
    if a * b == c:
        answer.add(c)
    a = make_num(n[:1])
    b = make_num(n[1:5])
    c = make_num(n[5:])
    if a * b == c:
        answer.add(c)
    count += 1
    
so = sum(answer)
    
    

