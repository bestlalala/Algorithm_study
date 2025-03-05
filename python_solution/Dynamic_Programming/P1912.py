# 연속합
import sys
input = sys.stdin.readline

n = int(input())
nums = [int(i) for i in input().split()]

s = [nums[0]]
for i in range(n-1):
    s.append(max(s[i] + nums[i+1], nums[i+1]))

print(max(s))

