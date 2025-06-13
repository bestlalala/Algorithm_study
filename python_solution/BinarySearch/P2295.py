# 2295번. 세 수의 합

n = int(input())
nums = []
for _ in range(n):
    nums.append(int(input()))

nums.sort()

# x + y = k - z

sums = set()
for x in nums:
    for y in nums:
        sums.add(x+y)

ans = []    # k값 리스트
for k in nums:
    for z in nums:
        if k-z in sums:
            ans.append(k)

ans.sort()
print(ans[-1])
