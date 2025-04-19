import math
import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
lst = [list(map(int, input().split())) for _ in range(m)]

dist = [[math.inf for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    dist[i][i] = 0

for a, b, d in lst:
    dist[a][b] = min(dist[a][b], d)

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[i][k] + dist[k][j]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if dist[i][j] == math.inf:
            dist[i][j] = 0

for i in range(1, n + 1):
    print(*dist[i][1:])
