from collections import deque

position = [(0, 1), (-1, 0), (0, -1), (1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]

while True:
    answer = 0
    w, h = input().split(' ')
    if w and h == '0':
        break

    w = int(w)
    h = int(h)

    maps = []
    for _ in range(int(h)):
        maps.append(input().split())
    visited = [[False for _ in range(w)] for _ in range(h)]
    queue = deque()
    for i in range(h):
        for j in range(w):
            if maps[i][j] == '1' and not visited[i][j]:
                queue.append([i, j])
                while queue:
                    row, col = queue.popleft()
                    for k in range(8):
                        nr, nc = row + position[k][0], col + position[k][1]
                        if 0 <= nr < h and 0 <= nc < w and maps[nr][nc] == '1' and not visited[nr][nc]:
                            queue.append([nr, nc])
                            visited[nr][nc] = True
                answer += 1
    print(answer)
