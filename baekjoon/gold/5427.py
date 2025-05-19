import sys
from collections import deque


def fire_extend(fire_board, fire):
    queue = deque()
    visited = [[False for _ in range(w)] for _ in range(h)]
    for time, r, c in fire:
        visited[r][c] = True
        queue.append((time, r, c))

    while queue:
        time, pr, pc = queue.popleft()

        for m in range(4):
            nr = pr + dr[m]
            nc = pc + dc[m]

            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr][nc] and lst[nr][nc] != '#':
                    visited[nr][nc] = True
                    fire_board[nr][nc] = time + 1
                    queue.append((time + 1, nr, nc))


input = sys.stdin.readline
T = int(input())
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

for t in range(T):
    w, h = list(map(int, input().split()))
    lst = [list(input().strip()) for _ in range(h)]
    fire_board = [[-1 for _ in range(w)] for _ in range(h)]
    s_board = [[-1 for _ in range(w)] for _ in range(h)]

    fire = []
    position = []

    for i in range(h):
        for j in range(w):
            if lst[i][j] == '*':
                fire.append((0, i, j))
            if lst[i][j] == '@':
                position.append((0, i, j))

    fire_extend(fire_board, fire)

    queue = deque(position)
    visited = [[False for _ in range(w)] for _ in range(h)]
    time, row, col = position[0]
    visited[row][col] = True

    if row == 0 or row == h - 1 or col == 0 or col == w - 1:
        print(1)
        continue

    escaped = False

    while queue:
        pt, pr, pc = queue.popleft()

        for m in range(4):
            nr = pr + dr[m]
            nc = pc + dc[m]

            if 0 <= nr < h and 0 <= nc < w:
                if not visited[nr][nc] and lst[nr][nc] == '.':
                    if fire_board[nr][nc] == -1 or pt + 1 < fire_board[nr][nc]:
                        visited[nr][nc] = True
                        s_board[nr][nc] = pt + 1
                        queue.append((pt + 1, nr, nc))
            else:
                print(pt + 1)
                escaped = True
                break
        if escaped:
            break

    if not escaped:
        print("IMPOSSIBLE")

