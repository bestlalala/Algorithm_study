# 5676번. 음주 코딩

import sys
input = sys.stdin.readline

def build_segtree(n, nums, N):
    segtree = [1] * (2 * N)
    
    # i + n 에 넣기
    for i in range(n):
        if nums[i] > 0:
            segtree[i+N] = 1
        elif nums[i] < 0:
            segtree[i+N] = -1
        else:
            segtree[i+N] = 0
    
    for i in range(N-1, 0, -1):
        segtree[i] = segtree[2 * i] * segtree[2 * i + 1]
    
    return segtree
            
# 변경 명령
def update(i, v, N, segtree):
    m = i + N - 1
    if v > 0:
        segtree[m] = 1
    elif v < 0:
        segtree[m] = -1
    else:
        segtree[m] = 0
    
    while m > 0:
        m //= 2
        segtree[m] = segtree[2 * m] * segtree[2 * m + 1]

# 곱셈 명령
def operation(i, j, segtree):
    if i == j:
        return segtree[i]
    # i: 짝, j: 홀
    if i % 2 == 0:
        if j % 2 != 0:
            return operation(i//2, j//2, segtree)
        # i: 짝, j: 짝
        else:
            return segtree[j] * operation(i//2, (j-1)//2, segtree)

    # i: 홀, j: 홀
    else:
        if j % 2 != 0:
            return segtree[i] * operation((i+1)//2, j//2, segtree)
        # i: 홀, J: 짝
        else:
            if i + 1 == j:
                return segtree[i] * segtree[j]
            else:
                return segtree[i] * segtree[j] * operation((i+1)//2, (j-1)//2, segtree)
    
while True:
    
    try :
        n, k = map(int, input().split())
        nums = list(map(int, input().split()))
        
        N = 1   # segtree 크기
        while n > N:
            N *= 2
        
        segtree = build_segtree(n, nums, N)
        # print(segtree)
        
        # round
        result = ""
        for _ in range(k):
            op, i, v = map(str, input().rstrip().split())
            i, v = int(i), int(v)
            # print("op", op, i, v)
            if op == 'C':
                update(i, v, N, segtree)
                # print(segtree)
            elif op == 'P':
                res = operation(i + N - 1, v + N - 1, segtree)
                # print("res", res)
                
                if res > 0:
                    result += '+'
                elif res < 0:
                    result += '-'
                else:
                    result += '0'
        print(result)
                
    except:
        break
