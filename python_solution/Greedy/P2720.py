# 2720번. 세탁소 사장 동혁

import sys
input = sys.stdin.readline

# 거스름돈의 액수 -> 리암이 줘야 할 동전 개수

money = [25, 10, 5, 1]

t = int(input().rstrip())
test_case = [int(input().rstrip()) for _ in range(t)]

for case in test_case:
    answer = []
    for m in money:
        answer.append(case // m)
        case %= m
    for a in answer:
        print(a, end=' ')
    print()
    