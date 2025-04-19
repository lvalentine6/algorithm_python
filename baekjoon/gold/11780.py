import math
import sys


def _find(route, i, j):
    if route[i][j] == 0:
        return [0]

    find_graph = [i]
    while i != j:
        i = route[i][j]
        find_graph.append(i)

    find_graph.insert(0, len(find_graph))

    return find_graph


input = sys.stdin.readline

n = int(input())
m = int(input())
lst = [list(map(int, input().split())) for _ in range(m)]

dist = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]
route = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for a, b, d in lst:
    if dist[a][b] > d:
        dist[a][b] = d
        route[a][b] = b

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]
                route[i][j] = route[i][k]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == math.inf:
            dist[i][j] = 0

for i in range(1, n + 1):
    print(*dist[i][1:])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(*_find(route, i, j))
