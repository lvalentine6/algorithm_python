import sys
from collections import deque

inputs = sys.stdin.readline


def solution():
    normal_result = 0
    ill_result = 0

    n = int(inputs())
    maps = [list(inputs().strip()) for _ in range(n)]
    normal_visited = [[False] * n for _ in range(n)]
    ill_visited = [[False] * n for _ in range(n)]
    lst = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def normal(r, c):
        queue = deque()
        queue.append((r, c))

        while queue:
            row, col = queue.popleft()
            color = maps[row][col]
            for dr, dc in lst:
                nr = row + dr
                nc = col + dc
                if 0 <= nr < n and 0 <= nc < n and maps[nr][nc] == color and not normal_visited[nr][nc]:
                    queue.append((nr, nc))
                    normal_visited[nr][nc] = True

    def ill(r, c):
        queue = deque()
        queue.append((r, c))

        while queue:
            row, col = queue.popleft()
            color = maps[row][col]
            temp = ('R', 'G')
            if color in temp:
                for dr, dc in lst:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < n and 0 <= nc < n and maps[nr][nc] != 'B' and not ill_visited[nr][nc]:
                        queue.append((nr, nc))
                        ill_visited[nr][nc] = True
            else:
                for dr, dc in lst:
                    nr = row + dr
                    nc = col + dc
                    if 0 <= nr < n and 0 <= nc < n and maps[nr][nc] == color and not ill_visited[nr][nc]:
                        queue.append((nr, nc))
                        ill_visited[nr][nc] = True

    for i in range(n):
        for j in range(n):
            if not normal_visited[i][j]:
                normal(i, j)
                normal_result += 1
            if not ill_visited[i][j]:
                ill(i, j)
                ill_result += 1

    print(normal_result, ill_result)


if __name__ == '__main__':
    solution()
