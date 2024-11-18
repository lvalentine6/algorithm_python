def dfs(row, col):
    moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    if dp[row][col] != -1:
        return dp[row][col]

    dp[row][col] = 1

    for direction in moves:
        nr = row + direction[0]
        nc = col + direction[1]

        if 0 <= nr < n and 0 <= nc < n and lst[row][col] < lst[nr][nc]:
            dp[row][col] = max(dp[row][col], dfs(nr, nc) + 1)

    return dp[row][col]

import sys
sys.setrecursionlimit(300000)

input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1 for _ in range(n)] for _ in range(n)]

answer = 0
for i in range(n):
    for j in range(n):
        answer = max(answer, dfs(i, j))

print(answer)
