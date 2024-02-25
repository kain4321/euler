
    


def select(num):
    b = []
    for i in range(0, num + 1):
        for i2 in range(0, num + 1):
            for i3 in range(0, num + 1):
                if i == i2:
                    continue
                if i == i3:
                    continue
                if i2 == i3:
                    continue
                
                b.append([i, i2, i3])
    return b 
        

d= select(2)
            
            