def MenOfPassion(A, n):
    cnt = 0
    sum = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            # print(i, j)
            sum = sum + A[i]*A[j]
            cnt += 1
            # print(cnt)
    return sum


A = [1, 2, 3, 4, 5, 6, 7, 8]

n = int(input())
# MenOfPassion(A, 7)
count = 0
for i in range(1, n):
    count += i
print(count)
print(2)
