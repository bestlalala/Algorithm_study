# 1049번. 기타줄

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

min_package, min_single = float('inf'), float('inf')
for _ in range(m):
    package, single = map(int, input().split())
    min_package = min(min_package, package)
    min_single = min(min_single, single)

cost1 = min_package * (n // 6 + 1)  # 패키지로만 사는 경우
cost2 = min_package * (n // 6) + min_single * (n % 6)    # 패키지 + 낱개
cost3 = min_single * n    # 낱개로만

print(min(cost1, cost2, cost3))
    