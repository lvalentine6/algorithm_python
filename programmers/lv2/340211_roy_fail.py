from collections import deque


def solution(points, routes):
    answer = 0

    board_r = 0
    board_c = 0

    for p in points:
        if p[0] > board_r:
            board_r = p[0]

        if p[1] > board_c:
            board_c = p[1]

    result_lst = []

    for r in routes:
        board = [[0 for col in range(board_c)] for row in range(board_r)]
        visited = [[False for col in range(board_c)] for row in range(board_r)]
        start = points[r[0] - 1]
        end = points[r[1] - 1]
        route_lst = []

        result_lst.append(bfs(board, start, end))

    max_size = 0

    for r in result_lst:
        if max_size < len(r):
            max_size = len(r)

    for idx in range(max_size):
        position_count = {}
    for p in result_lst:
        if idx < len(p):
            position = p[idx]
            if position in position_count:
                position_count[position] += 1
            else:
                position_count[position] = 1

    for count in position_count.values():
        if count > 1:
            answer += 1

    return answer


def bfs(board, start, end):
    rows, cols = len(board), len(board[0])
    queue = deque([(start[0] - 1, start[1] - 1, 0)])  # (row, col, distance)
    visited = set([(start[0] - 1, start[1] - 1)])
    parent = {}

    while queue:
        row, col, dist = queue.popleft()

        if (row, col) == (end[0] - 1, end[1] - 1):
            return reconstruct_path(parent, (start[0] - 1, start[1] - 1), (end[0] - 1, end[1] - 1))

        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = row + dr, col + dc
            if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                queue.append((nr, nc, dist + 1))
                visited.add((nr, nc))
                parent[(nr, nc)] = (row, col)


def reconstruct_path(parent, start, end):
    path = []
    current = end
    while current != start:
        path.append(current)
        current = parent[current]
    path.append(start)
    return path[::-1]
