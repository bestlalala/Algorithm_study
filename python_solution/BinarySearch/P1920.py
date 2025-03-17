# 1920번. 수 찾기
import sys
input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().split()))
m = int(input().rstrip())
test_case = list(map(int, input().split()))

nums.sort()

def binary_search(target, data):
    left, right = 0, len(data)-1
    
    while left <= right:
        mid = (left + right) // 2
        
        if data[mid] < target:
            left = mid + 1
        elif data[mid] > target:
            right = mid -1
        else:
            return 1
    return 0
            
for case in test_case:
    print(binary_search(case, nums))