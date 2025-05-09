# 20920번. 영단어 암기는 괴로워

import sys
import collections
input = sys.stdin.readline

n, m = map(int, input().split())

words = []
for _ in range(n):
    word = input().rstrip()
    if len(word) >= m:
        words.append(word)

word_cnt = collections.Counter(words)
res = list(word_cnt.items())
res.sort(key=lambda x: (-x[1], -len(x[0]), x[0]))

for w, c in res:
    print(w)