import sys
from collections import deque

input = sys.stdin.readline
t = int(input())
dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [-2, -1, 1, 2, 2, 1, -1, -2]

for _ in range(t):
    n = int(input())
    start = list(map(int, input().split(' ')))
    target = list(map(int, input().split(' ')))
    visited = [[False for _ in range(n)] for _ in range(n)]
    answer = 0

    sr, sc = start
    queue = deque()
    queue.append((sr, sc, 0))
    visited[sr][sc] = True

    while queue:
        pr, pc, cnt = queue.popleft()

        if pr == target[0] and pc == target[1]:
            answer = cnt
            break

        for i in range(8):
            nr = pr + dr[i]
            nc = pc + dc[i]

            if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                visited[nr][nc] = True
                queue.append((nr, nc, cnt + 1))

    print(answer)
