import sys

input = sys.stdin.readline
n = int(input())
calendar = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]

for i in range(n):
    p, m = calendar[i]
    dp[i + 1] = max(dp[i], dp[i + 1])
    if i + p > n:
        continue
    dp[i + p] = max(dp[i + p], dp[i] + m)

print(max(dp))
