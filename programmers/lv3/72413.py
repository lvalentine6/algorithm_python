import math


def solution(n, s, a, b, fares):
    answer = 0

    graph = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        graph[i][i] = 0

    for i, j, d in fares:
        graph[i][j] = d
        graph[j][i] = d

    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if graph[i][j] > graph[i][k] + graph[k][j]:
                    graph[i][j] = graph[i][k] + graph[k][j]

    dist = []

    for i in range(1, n + 1):
        _sum = 0
        _sum += graph[s][i]
        _sum += graph[i][a] + graph[i][b]
        dist.append(_sum)

    answer = min(graph[s][a] + graph[s][b], min(dist))

    return answer
