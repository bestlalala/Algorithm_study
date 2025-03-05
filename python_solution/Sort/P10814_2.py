# 10814번 다른 풀이

n = int(input())
judge_list = []

for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    judge_list.append((age, name))

judge_list.sort(key=lambda x: x[0])

for i in judge_list:
    print(i[0], i[1])