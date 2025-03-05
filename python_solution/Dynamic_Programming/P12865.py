# 12865번. 평범한 배낭

n, k = map(int, input().split())
bags = [[int(m) for m in input().split()] for _ in range(n)]


def knapSack_dp():
    A = [[0 for x in range(k+1)] for x in range(n+1)]

    for i in range(1, n+1):
        for w in range(1, k+1):
            if bags[i-1][0] > w:
                A[i][w] = A[i-1][w]
            else:
                valWith = bags[i-1][1] + A[i-1][w-bags[i-1][0]]
                valWithout = A[i-1][w]
                A[i][w] = max(valWith, valWithout)
    return A[n][w]


print(knapSack_dp())

