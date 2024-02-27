def fib(num):
    count = 3
    f1 = 1
    f2 = 1
    f3 = 2
    while True:
        f1 = f2 + f3
        count += 1
        if f1 >= num:
            break
        f2 = f1 + f3
        count += 1
        if f2 >= num:
            break
        f3 = f1 + f2
        count += 1
        if f3 >= num:
            break
    return f1, f2, f3, count

number = 10**999
result = fib(number)


        