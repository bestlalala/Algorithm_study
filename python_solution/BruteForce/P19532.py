# 수학은 비대면 강의입니다.

nums = [int(n) for n in input().split()]

flag = True
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (nums[0]*x + nums[1]*y == nums[2]) and (nums[3]*x + nums[4]*y == nums[5]):
            print(x, y)
            flag = False
    if not flag:
        break

