import sys

sys.setrecursionlimit(100000)


def dfs(position, target, p_cnt, route, k, n, m):
    global answer
    if answer:
        return

    tr, tc = target
    pr, pc = position

    remain = k - p_cnt
    dist = abs(pr - tr) + abs(pc - tc)

    if remain < dist or (remain - dist) % 2 != 0:
        return

    if pr == tr and pc == tc and p_cnt == k:
        answer = route
        return

    for i in range(4):
        nr = pr + dr[i]
        nc = pc + dc[i]

        if 0 <= nr < n and 0 <= nc < m:
            dfs((nr, nc), (tr, tc), p_cnt + 1, route + chars[i], k, n, m)


def solution(n, m, x, y, r, c, k):
    global result
    global answer
    answer = ''
    global dr
    global dc
    global chars

    dr = [1, 0, 0, -1]
    dc = [0, -1, 1, 0]
    chars = ['d', 'l', 'r', 'u']

    dfs((x - 1, y - 1), (r - 1, c - 1), 0, '', k, n, m)

    if not answer:
        answer = 'impossible'

    return answer
