# 9465번. 스티커

import sys
from collections import deque
input = sys.stdin.readline

# 상냥이가 뗄 수 있는 스티커의 점수의 최댓값 구하기
# 점수의 합이 최대 & 서로 변을 공유하지 않는 스티커 집합

t = int(input().rstrip())
for _ in range(t):
    n = int(input().rstrip())
    sticker = [list(map(int, input().split())) for _ in range(2)]

    if n == 1:  # 열이 하나 뿐일 때는 최댓값을 단순 비교
        print(max(sticker[0][0], sticker[1][0]))
        continue
    
    # DP 테이블 초기화 (열이 2개 이상일 때)
    dp = [[0] * n for _ in range(2)]
    dp[0][0] = sticker[0][0]
    dp[1][0] = sticker[1][0]
    
    # 두 번째 열의 값 초기화
    dp[0][1] = sticker[0][1] + dp[1][0]
    dp[1][1] = sticker[1][1] + dp[0][0]
    
    # DP 테이블 채우기
    for i in range(2, n):
        dp[0][i] = sticker[0][i] + max(dp[1][i-1], dp[1][i-2])
        dp[1][i] = sticker[1][i] + max(dp[0][i-1], dp[0][i-2])
        
    # 최댓값 출력
    print(max(dp[0][n-1], dp[1][n-1]))

