# 쉬운 계단 수

n = int(input())

# DP 테이블 초기화
dp = [[0]*10 for _ in range(n+1)]

# 1의 자릿수의 경우의 수 초기화
for i in range(1, 10):
    dp[1][i] = 1

# 나머지 자릿수의 경우의 수 탐색
for i in range(2, n+1):
    for j in range(10):
        # 가장 뒤에 오는 숫자가 0일 때에는 그 앞에 1만 올 수 있다.
        if j == 0:
            dp[i][j] = dp[i-1][1]
        # 가장 뒤에 오는 숫자가 1~8일 때에는 그 앞에 +-1이 올 수 있다.
        elif 1 <= j <= 8:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
        # 가장 뒤에 오는 숫자가 9일 때에는 그 앞에 8만 올 수 있다.
        else:
            dp[i][j] = dp[i-1][8]

print(sum(dp[n]) % 1000000000)

