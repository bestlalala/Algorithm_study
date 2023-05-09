# 수 정렬하기 3
import sys

n = int(sys.stdin.readline())

nums = [0] * 10000
for _ in range(n):
    nums[int(sys.stdin.readline())-1] += 1

for i in range(10000):
    if nums[i] != 0:
        for j in range(nums[i]):
            print(i+1)

