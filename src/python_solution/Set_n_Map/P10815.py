# 10815번 - 숫자 카드
import sys
input = sys.stdin.readline

n = int(input())
nums = set(int(n) for n in input().split())

m = int(input())
cards = [int(n) for n in input().split()]

for i in cards:
    if i in nums:
        print(1, end=' ')
    else:
        print(0, end=' ')
