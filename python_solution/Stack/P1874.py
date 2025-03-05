# 1874번. 스택 수열

n = int(input())

# 4 3 6 8 7 5 2 1

# 1 2 3 4 --> 4
# 1 2 3 --> 3
# 1 2 5 6 --> 6
# 1 2 5 7 8 --> 8
# 1 2 5 7 --> 7
# 1 2 5 --> 5
# 1 2 --> 2
# 1 --> 1


stack = list()
answer = list()
flag = 0
cur = 1
for i in range(n):
    num = int(input())

    # cur == num 일 때까지 돌면서 스택을 쌓는다.
    while cur <= num:
        stack.append(cur)
        answer.append('+')
        cur += 1
        # 입력한 수를 만나면 while문 탈출

    if stack[-1] == num:
        stack.pop()  # 스택의 Top 을 꺼내 수열을 만들어 준다.
        answer.append('-')
    # stack 의 TOP 이 입력한 숫자가 아니면 주어진 스택을 만들 수 없다.
    else:
        print("NO")
        flag = 1
        break

if flag == 0:
    for i in answer:
        print(i)

