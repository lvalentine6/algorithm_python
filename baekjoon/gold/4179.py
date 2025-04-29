import sys
from collections import deque


def fire_extend(board, f_board, f_visited, start):
    queue = deque()
    for s in start:
        queue.append(s)
        f_visited[s[0]][s[1]] = True

    while queue:
        pr, pc, t = queue.popleft()
        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]

            if 0 <= nr < r and 0 <= nc < c:
                if not f_visited[nr][nc] and board[nr][nc] != '#':
                    f_visited[nr][nc] = True
                    f_board[nr][nc] = t
                    queue.append((nr, nc, t + 1))


def bfs(board, f_board, visited, start):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True

    while queue:
        pr, pc, time = queue.popleft()
        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]

            if nr < 0 or nr >= r or nc < 0 or nc >= c:
                print(time)
                exit()

            if board[nr][nc] == '.' and not visited[nr][nc]:
                if f_board[nr][nc] == -1 or time < f_board[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, time + 1))


input = sys.stdin.readline
global r, c
r, c = list(map(int, input().split()))
j_start, f_start = (), []
board = [list(input().strip()) for _ in range(r)]
f_board = [[-1 for _ in range(c)] for _ in range(r)]

j_visited = [[False for _ in range(c)] for _ in range(r)]
f_visited = [[False for _ in range(c)] for _ in range(r)]
global dr, dc
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            j_start = (i, j, 1)
        elif board[i][j] == 'F':
            f_start.append((i, j, 1))

fire_extend(board, f_board, f_visited, f_start)
bfs(board, f_board, j_visited, j_start)

print('IMPOSSIBLE')
