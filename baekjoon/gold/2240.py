import sys

input = sys.stdin.readline

t, w = list(map(int, input().split()))
lst = [int(input()) for _ in range(t)]
dp = [[0 for _ in range(w + 1)] for _ in range(t + 1)]

for i in range(1, t + 1):
    for j in range(w + 1):
        dp[i][j] = dp[i - 1][j]

        if j > 0:
            dp[i][j] = max(dp[i - 1][j - 1], dp[i][j])

        moved = 0
        if j % 2 == 0:
            moved = 1
        else:
            moved = 2

        if lst[i - 1] == moved:
            dp[i][j] += 1

print(max(dp[t]))
