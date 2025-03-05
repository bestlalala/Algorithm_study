# 1744번. 수 묶기

# 양수: 가장 큰 수 기준 정렬로 곱하기
# 음수: 가장 작은 수 기준 정렬로 곱하기
# 1: 무조건 더해주기
# 0: 마지막으로 남은 음수값을 0과 곱하기 -> 음수 배열에 넣기

n = int(input())
plus = []
minus = []

result = 0

for _ in range(n):
    num = int(input())
    if num > 1:
        plus.append(num)
    elif num <= 0:
        minus.append(num)
    else:
        result += num

# 정렬
plus.sort(reverse=True)
minus.sort()


def muggki(L):
    sum = 0
    for i in range(0, len(L), 2):
        if i + 1 >= len(L):
            sum += L[i]
        else:
            sum += L[i] * L[i + 1]
    return sum


result += muggki(plus) + muggki(minus)
print(result)

