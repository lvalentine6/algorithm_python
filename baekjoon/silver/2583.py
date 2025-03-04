import sys
from collections import deque


def bfs(row, col):
    queue = deque()
    queue.append((row, col))
    cnt = 1

    while queue:
        pr, pc = queue.popleft()

        for idx in range(4):
            nr = pr + dr[idx]
            nc = pc + dc[idx]

            if 0 <= nr < m and 0 <= nc < n:
                if not visited[nr][nc] and lst[nr][nc] == 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
                    cnt += 1

    return cnt


input = sys.stdin.readline

m, n, k = list(map(int, input().split()))

lst = [[0 for _ in range(n)] for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]
dr = [1, -1, 0, 0]
dc = [0, 0, -1, 1]
count = 0
result = []

for i in range(k):
    start_row, start_col, end_row, end_col = list(map(int, input().split()))
    for j in range(start_col, end_col):
        for r in range(start_row, end_row):
            lst[j][r] = 1

for i in range(m):
    for j in range(n):
        if not visited[i][j] and lst[i][j] == 0:
            visited[i][j] = True
            result.append(bfs(i, j))
            count += 1

result.sort()

print(count)
print(*result)
