import heapq
import math


def dijkstra(board, lst, cost, row, col):
    queue = []
    heapq.heappush(queue, (cost, row, col, 0))
    heapq.heappush(queue, (cost, row, col, 1))

    while queue:
        p_cost, pr, pc, pd = heapq.heappop(queue)

        if pr == n - 1 and pc == n - 1:
            return min(lst[pr][pc])

        for i in range(4):
            nr = pr + dr[i]
            nc = pc + dc[i]

            if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
                if pd == i:
                    n_cost = p_cost + 100
                else:
                    n_cost = p_cost + 600

                if n_cost < lst[nr][nc][i]:
                    lst[nr][nc][i] = n_cost
                    heapq.heappush(queue, (n_cost, nr, nc, i))


def solution(board):
    global n
    n = len(board)
    answer = 0

    global dr
    global dc

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    lst = [[[math.inf] * 4 for _ in range(n)] for _ in range(n)]

    answer = dijkstra(board, lst, 0, 0, 0)

    return answer
