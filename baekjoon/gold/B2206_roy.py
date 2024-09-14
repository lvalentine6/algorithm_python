import sys
from collections import deque

inputs = sys.stdin.readline


def solution():
    n, m = map(int, inputs().split())
    maps = [list(inputs().strip()) for _ in range(n)]
    visited = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    result = 0
    visited[0][0][1] = 1
    move = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    queue = deque([(0, 0, 1)])

    while queue:
        row, col, skill = queue.popleft()

        if row == n - 1 and col == m - 1:
            result = visited[row][col][skill]
            break

        for dr, dc in move:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m:
                # 벽이 아니고 방문하지 않은 경우
                if maps[nr][nc] == '0' and visited[nr][nc][skill] == 0:
                    visited[nr][nc][skill] = visited[row][col][skill] + 1
                    queue.append((nr, nc, skill))
                # 벽이고, 벽을 부술수 있을때
                elif maps[nr][nc] == '1' and skill == 1:
                    visited[nr][nc][0] = visited[row][col][skill] + 1
                    queue.append((nr, nc, 0))

    print(result) if result != 0 else print(-1)


if __name__ == '__main__':
    solution()
