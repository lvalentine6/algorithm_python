from collections import deque


def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[-1 for _ in range(m)] for _ in range(n)]
    queue = deque([(0, 0)])
    visited[0][0] = 1

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1 and visited[nx][ny] == -1:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    return visited[n - 1][m - 1]
