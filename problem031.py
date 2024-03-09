target = 200
coin_sizes = [1, 2, 5, 10, 20, 50, 100, 200]
ways = [0]*(target+1)
ways[0] = 1
for coin in coin_sizes:
    for money in range(coin, target + 1):
        ways[money] += ways[money - coin]
answer = ways[-1]