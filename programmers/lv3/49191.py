import math


def solution(n, results):
    answer = 0

    lst = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i == j:
                lst[i][j] = 0

    for r in results:
        w, l = r
        lst[w][l] = 1

    for k in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                if lst[a][k] != math.inf and lst[k][b] != math.inf:
                    lst[a][b] = min(lst[a][b], lst[a][k] + lst[k][b])

    for i in range(1, n + 1):
        cnt = 0
        for j in range(1, n + 1):
            if i != j and (lst[i][j] != math.inf or lst[j][i] != math.inf):
                cnt += 1
        if cnt == n - 1:
            answer += 1

    return answer
