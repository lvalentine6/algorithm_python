import sys
from collections import deque


def fire_extend(board, f_board, fire_lst):
    moved_fire = []

    for f in fire_lst:
        for i in range(4):
            nr = f[0] + dr[i]
            nc = f[1] + dc[i]

            if 0 <= nr < r and 0 <= nc < c:
                if board[nr][nc] != '#':
                    board[nr][nc] = 'F'
                    moved_fire.append((nr, nc))

    return moved_fire

def bfs(board, start, visited, fire_lst):
    queue = deque()
    queue.append(start)
    visited[start[0]][start[1]] = True
    result = 0

    while queue:
        pr, pc, time = queue.popleft()
        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]

            if 0 <= nr < r and 0 <= nc < c:
                if board[nr][nc] == '.':
                    visited[nr][nc] = True
                    queue.append((nr, nc, time + 1))
            else:
                return time

    return result


input = sys.stdin.readline
global r, c
r, c = list(map(int, input().split()))
start, fired = (), ()
board = [list(input().strip()) for _ in range(r)]
j_board = [[-1 for _ in range(r)] for _ in range(c)]
f_board = [[-1 for _ in range(r)] for _ in range(c)]

visited = [[False for _ in range(c)] for _ in range(r)]
global dr, dc
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for i in range(r):
    for j in range(c):
        if board[i][j] == 'J':
            start = (i, j, 1)
        elif board[i][j] == 'F':
            fired = (i, j)

fire_extend()


print(bfs(board, start, visited, fired))
