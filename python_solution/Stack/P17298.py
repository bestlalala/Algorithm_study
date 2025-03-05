# 17298번. 오큰수

n = int(input())
nums = [int(i) for i in input().split()]

stack = []  # 원소의 인덱스 넣어주기
ans = [-1] * n

stack.append(0)
for i in range(1, n):
    while stack:
        if nums[stack[-1]] < nums[i]:
            ans[stack.pop()] = nums[i]
        else:
            break
    stack.append(i)

print(*ans)
