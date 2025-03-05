# 11047번. 동전 0

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

coins.sort(reverse=True)

count = []
for i in range(n):
    cnt = k // coins[i]
    count.append(cnt)
    k -= cnt * coins[i]

print(sum(count))
