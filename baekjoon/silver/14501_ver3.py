n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [0 for _ in range(n + 1)]

for i in range(n)[::-1]:
    if i + lst[i][0] > n:
        dp[i] = dp[i + 1]
    else:
        dp[i] = max(dp[i + lst[i][0]] + lst[i][1], dp[i + 1])

print(dp[0])
