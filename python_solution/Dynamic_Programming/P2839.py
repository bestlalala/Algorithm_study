# 2839번. 설탕 배달

import sys
input = sys.stdin.readline

INF = int(1e9)

n = int(input())

# dp[i] = 정확히 i kg를 만들기 위해 필요한 최소 봉지 수
dp = [INF] * (n+1)

dp[0] = 0
for i in range(3, n+1):
    if i >=3 and dp[i-3] != INF:
        dp[i] = min(dp[i], dp[i-3] + 1)
    if i >= 5 and dp[i-5] != INF:
        dp[i] = min(dp[i], dp[i-5] + 1)

    
print(dp[n] if dp[n] != INF else -1)

# cnt = 0
# while n >= 0:
#     if n % 5 == 0:
#        print(cnt + n // 5)
#        exit(0)
#     else:
#         n -= 3
#         cnt += 1 

# print(-1)