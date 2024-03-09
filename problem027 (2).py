def is_prime(num):
    if num <= 0:
        return False
    prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            prime = False
    return prime


def making(a, b):
    n = 1
    while True:
        if is_prime(n**2 + a*n + b) == False:
            break
        n += 1
    return n-1


test = []
test2 = []
for a in range(-999, 1000):
    for b in range(-999, 1000):
        test.append(making(a, b))
        test2.append(a*b)


result = max(test)
answer = test.index(result)
f = test2[answer]

