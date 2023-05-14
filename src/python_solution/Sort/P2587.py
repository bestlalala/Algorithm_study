# 대표값2

nums = []
for i in range(5):
    nums.append(int(input()))

sum = 0
for i in range(5):
    sum += nums[i]

avg = sum // 5
nums.sort()

print(avg)
print(nums[2])

