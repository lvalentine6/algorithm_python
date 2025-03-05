import sys
from collections import deque


def bfs(row, col):
    queue = deque()
    queue.append((row, col))

    while queue:
        pr, pc = queue.popleft()

        for idx in range(4):
            nr = pr + dr[idx]
            nc = pc + dc[idx]

            if 0 <= nr < n and 0 <= nc < n:
                if not visited[nr][nc] and not submerged[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))


input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
max_length = max(max(lst))
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
result = []

for i in range(0, 100):
    submerged = [[False for _ in range(n)] for _ in range(n)]
    visited = [[False for _ in range(n)] for _ in range(n)]
    count = 0
    for j in range(n):
        for k in range(n):
            if lst[j][k] <= i:
                submerged[j][k] = True

    for j in range(n):
        for k in range(n):
            if not submerged[j][k] and not visited[j][k]:
                visited[j][k] = True
                bfs(j, k)
                count += 1

    result.append(count)

print(max(result))
