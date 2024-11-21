from collections import deque


def bfs(row, col):
    queue = deque()
    visited = [[False] * m for _ in range(n)]

    queue.append((row, col, 0))
    visited[row][col] = True
    max_depth = 0

    while queue:
        pr, pc, d = queue.popleft()
        max_depth = d

        for move in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = pr + move[0]
            nc = pc + move[1]

            if 0 <= nr < n and 0 <= nc < m and not visited[nr][nc] and lst[nr][nc] == 'L':
                visited[nr][nc] = True
                queue.append((nr, nc, d + 1))

    return max_depth


import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(input().strip()) for _ in range(n)]
result = 0

for i in range(n):
    for j in range(m):
        if lst[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
