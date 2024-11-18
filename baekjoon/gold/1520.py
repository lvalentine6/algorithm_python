def dfs(row, col):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    if row == n - 1 and col == m - 1:
        return 1

    if dp[row][col] != -1:
        return dp[row][col]

    dp[row][col] = 0

    for direction in moves:
        nr = row + direction[0]
        nc = col + direction[1]

        if 0 <= nr < n and 0 <= nc < m and lst[row][col] > lst[nr][nc]:
            dp[row][col] += dfs(nr, nc)

    return dp[row][col]

import sys

sys.setrecursionlimit(300000)

input = sys.stdin.readline

n, m = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]

print(dfs(0, 0))
