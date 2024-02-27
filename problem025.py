count = 0        
f1 = 1
f2 = 1
f3 = 2
num = 10**2 
while True:
    count += 1
    f2  = f1 + f3
    count += 1
    if f2 >= num:
        break
    f1 = f2 = 1 + f3
    count += 1
    if f1 >= num:
        break
    f3 = f2 + f1
    count += 1
    if f3 >= num:
        break
    print(f1, f2, f3)
    
print(dasdd)
