# 분해합

n = int(input())

for i in range(1, n+1):
    num = sum(map(int, str(i)))
    n_sum = i + num

    if n_sum == n:
        print(i)
        break
    if i == n:
        print(0)

