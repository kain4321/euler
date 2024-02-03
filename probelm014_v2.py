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


