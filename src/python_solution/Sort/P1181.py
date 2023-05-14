# 단어 정렬

n = int(input())

words = []
for i in range(n):
    words.append(input())

# 중복 제거
words = list(set(words))

words.sort()
words.sort(key=lambda x: len(x))

for w in words:
    print(w)