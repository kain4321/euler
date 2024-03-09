def find_len(num):
    count = 1
    a = []
    ten = 10**count
    while num != 0:
        a.append(num%ten)
        num = num // ten
        count += 1
    return a
        
def find_num(num):
    a = []
    num1 = find_len(num)
    count = 0
    while count != len(num1):
        a.append(num1[count] ** 5)
        count += 1
    return sum(a)

num1 = 1
a = []
while num1 <= 1000000:
    num1 += 1
    if num1 == find_num(num1):
        a.append(num1)
     
        
b = sum(a)
    