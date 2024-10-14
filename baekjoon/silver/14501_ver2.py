def recur(idx):
    if idx == n:
        return 0

    if idx > n:
        return -99999

    if dp[idx] != -1:
        return dp[idx]

    dp[idx] = max(recur(idx + lst[idx][0]) + lst[idx][1], recur(idx + 1))

    print(dp)
    return dp[idx]

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [-1 for _ in range(n+1)]

recur(0)

print(dp[0])
