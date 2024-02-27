def is_prime(num):
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
    return prime


def making():
    num1 = 2
    count = []
    while True:
        if len(count) == 5:
            break
        for n in range (0, num1):
            for a in range(-999, 1000):
                for b in range(-999, 1000):
                    if is_prime(n**2 + a*n + b) == False:
                        num1 += 1
                    if is_prime(n**2 + a*n + b) == True:
                        count.append(n**2, a*n, b)
    return count
    
                        
    
a = making()
