# 블랙잭
n, m = map(int, input().split())
nums = [int(n) for n in input().split()]

max = 0
for i in range(n-2):
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = nums[i] + nums[j] + nums[k]
            if max < sum <= m:
                max = sum

print(max)
