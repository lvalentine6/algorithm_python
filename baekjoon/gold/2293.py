import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))
lst = [int(input()) for _ in range(n)]
answer = 0

dp = [0 for _ in range(k + 1)]
dp[0] = 1

for coin in lst:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]

print(dp[k])
