import sys

input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] * 3 for _ in range(n)]

for i in range(n):
    for j in range(3):
        if j == 0:
            dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + lst[i][j]
        if j == 1:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][2]) + lst[i][j]
        if j == 2:
            dp[i][j] = min(dp[i - 1][0], dp[i - 1][1]) + lst[i][j]

print(min(dp[::-1][0]))
