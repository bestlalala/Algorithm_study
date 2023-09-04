# 11399번. ATM

n = int(input())
P = [int(m) for m in input().split()]

result = 0
time = 0
for i in range(n):
    time += P.pop(P.index(min(P)))
    result += time

print(result)