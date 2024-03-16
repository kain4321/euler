def check_prime(num):
    if num <= 1:
        return False
    is_prime = True
    for a in range(2, int(num**0.5) + 1):
        if num % a == 0:
            is_prime = False
            break
    return is_prime

def right_side(num):
    length = len(num)
    count = 1
    result = []
    while count != length:
        result.append(int(num[:count]))
        count += 1
    return result

def left_side(num):
    length = len(num)
    count = 1
    result = []
    while count != length:
        result.append(int(num[count:]))
        count += 1
    return result

result = set()
result1 = set()
for i in range(10, 1000000):
    prime = True
    if check_prime(i) == True:
        a = left_side(str(i))
        for number in a:
            if check_prime(number) == False:
                prime = False
        if prime:
            result.add(i)
    prime = True
    if check_prime(i) == True:
        b = right_side(str(i))
        for number in b:
            if check_prime(number) == False:
                prime = False
        if prime:
            result1.add(i)
            
common = result.intersection(result1)
answer = sum(common)
            
    
    
    