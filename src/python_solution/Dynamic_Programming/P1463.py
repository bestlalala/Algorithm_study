# 1로 만들기

n = int(input())

x = [0] * (n+1)

for i in range(2, n+1):
    x[i] = x[i-1] + 1
    if n % 3 == 0:
        x[i] = min(x[i], x[i//3] + 1)
    if n % 2 == 0:
        x[i] = min(x[i], x[i//2] + 1)
print(x[n])

