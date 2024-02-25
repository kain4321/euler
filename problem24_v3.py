num = 4
b = []
for i in range(0, num):
    for i2 in range(0, num):
        for i3 in range(0, num):
            for i4 in range(0, num):
                if i == i2:
                    continue
                if i == i3:
                    continue
                if i2 == i3:
                    continue
                b.append([i, i2, i3])