# 11501번. 주식
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    stock = [int(m) for m in input().split()]
    profit = 0
    max_price = 0
    for i in range(n-1, -1, -1):
        if stock[i] > max_price:
            max_price = stock[i]
        else:
            profit += max_price-stock[i]

    print(profit)
