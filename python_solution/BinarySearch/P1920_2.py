# 1920번. 수 찾기

n = int(input())
nums = list(map(int, input().split()))

m = int(input())
xs = list(map(int, input().split()))

nums.sort()

def binary_search(nums, target):
    low, high = 0, n-1

    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            return 1
    
    return 0

for x in xs:
    print(binary_search(nums, x))
