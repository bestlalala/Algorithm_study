n = int(input())
nums = list(map(int, input().split()))
m = int(input())
cards = list(map(int, input().split()))

dic = {}

for c in cards:
    dic[c] = 0

for i in nums:
    if i in dic:
        dic[i] = 1

for d in dic:
    print(dic[d], end=' ')

