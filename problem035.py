def check_prime(num):
    if num == 1:
        return False
    is_prime = True
    for a in range(2, int(num**0.5) + 1):
        if num % a == 0:
            is_prime = False
            break
    return is_prime

def flipping(number):
    result = [number]
    number_str = str(number)
    length = len(number_str)
    for index in range(length):
        if index == 0:
            continue
        new_str = number_str[-index:] + number_str[:length-index]
        result.append(int(new_str))
    return result

result = set()
for a in range(1, 101):
    is_all_prime = True
    flipped = flipping(a)
    for number in flipped:
        if check_prime(number) == False:
            is_all_prime = False
            break
    if is_all_prime:
        result.add(a)
    # if check_prime(a) == True:
    #     flipped = flipping(a)
    #     for number in flipped:
    #         if check_prime(number) == True:
    #                 result.add(a)
            
    
 
    
     


