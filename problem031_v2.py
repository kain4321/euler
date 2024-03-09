target = 200
coin_sizes = [1, 2, 5, 10, 20, 50, 100, 200]
a = [0] * (target + 1)
a[0] = 1 
for i in coin_sizes:
    for b in range(i, target + 1):
        a[b] += a[b - i]
n = target       
answer = a[n]