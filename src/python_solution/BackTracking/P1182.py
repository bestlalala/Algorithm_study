# 1182번. 부분수열의 합

n, s = map(int, input().split())
nums = [int(i) for i in input().split()]
cnt = 0
ans = []


def solve(start):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1

    for i in range(start, n):
        ans.append(nums[i])
        solve(i+1)
        ans.pop()


solve(0)
print(cnt)


