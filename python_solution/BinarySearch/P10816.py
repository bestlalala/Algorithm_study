# 10816번. 숫자 카드 2
import collections

n = int(input())
mycards = collections.Counter(list(map(int, input().split())))

m = int(input())
nums = list(map(int, input().split()))

for num in nums:
    print(mycards[num], end=' ')

