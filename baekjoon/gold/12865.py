def recur(idx, w):
    if w > k:
        return -9999

    if idx == n:
        return 0

    if dp[idx][w] != -1:
        return dp[idx][w]

    dp[idx][w] = max(recur(idx + 1, w + lst[idx][0]) + lst[idx][1], recur(idx + 1, w))

    return dp[idx][w]


n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(100001)] for _ in range(n)]

recur(0, 0)

print(dp[0][0])
