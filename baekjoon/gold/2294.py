import math
import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))
lst = [int(input()) for _ in range(n)]
answer = 0

dp = [math.inf for _ in range(k + 1)]
dp[0] = 0

for coin in lst:
    for i in range(coin, k + 1):
        dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[k] if dp[k] != math.inf else -1)
