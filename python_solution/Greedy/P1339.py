# 1339번. 단어 수학

import sys
import collections
input = sys.stdin.readline

n = int(input())
words = [input().rstrip() for _ in range(n)]

# 자릿수별로 가중치를 계산하고, 그걸 정렬
weights = collections.defaultdict(int)

for word in words:
    for idx, char in enumerate(word):
        weights[char] = weights[char] + 10 ** (len(word) - idx - 1)

# 가중치가 큰 알파벳부터 큰 숫자 할당
sorted_chars = sorted(weights.items(), key=lambda x: x[1], reverse=True)

num = 9
res = 0
for char, weight in sorted_chars:
    res += weight * num
    num -= 1

print(res)
