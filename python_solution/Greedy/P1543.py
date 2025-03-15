# 1543번. 문서 검색
import sys
input = sys.stdin.readline

doc = input().rstrip()
word = input().rstrip()

doc_n = len(doc)
n = len(word)
cnt, i = 0, 0

while i <= doc_n-n:
    if doc[i:i+n] == word:
        cnt += 1
        i += n
    else:
        i += 1

print(cnt)
        