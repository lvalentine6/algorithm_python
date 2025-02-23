import sys

sys.setrecursionlimit(1000000)


def dfs(position):
    px, py = position
    size = 1

    for k in range(4):
        nx = px + dx[k]
        ny = py + dy[k]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and lst[nx][ny] == 1:
                visited[nx][ny] = True
                size += dfs((nx, ny))

    return size


input = sys.stdin.readline

n, m = list(map(int, (input().split())))
lst = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
count = 0
max_size = 0

for i in range(n):
    for j in range(m):
        if not visited[i][j] and lst[i][j] == 1:
            visited[i][j] = True
            max_size = max(dfs((i, j)), max_size)
            count += 1

print(count)
print(max_size)
