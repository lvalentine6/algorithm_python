import sys
from collections import deque


def check(lst, removes, start):
    queue = deque([start])
    visited = [[False for _ in range(6)] for _ in range(12)]
    pr, pc, c = start
    visited[pr][pc] = True
    positions = [(pr, pc)]

    while queue:
        pr, pc, c = queue.popleft()

        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]

            if 0 <= nr < 12 and 0 <= nc < 6:
                if not visited[nr][nc] and lst[nr][nc] == c:
                    visited[nr][nc] = True
                    queue.append((nr, nc, c))
                    positions.append((nr, nc))

    if len(positions) >= 4:
        for p in positions:
            removes.add(p)


input = sys.stdin.readline
lst = [list(input().strip()) for _ in range(12)]
answer = 0

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

while True:

    removes = set()

    for i in range(12):
        for j in range(6):
            if lst[i][j] != '.':
                check(lst, removes, (i, j, lst[i][j]))

    removes = sorted(list(removes))

    if not removes:
        break

    for row, col in removes:
        tmp = deque()
        for k in range(row + 1):
            tmp.append(lst[k][col])
        tmp.pop()
        tmp.appendleft('.')
        for k in range(row + 1):
            lst[k][col] = tmp.popleft()

    answer += 1

print(answer)
