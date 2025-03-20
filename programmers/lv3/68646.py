import math


def solution(a):
    answer = 0
    n = len(a)

    left_dp = [math.inf for _ in range(n)]
    right_dp = [math.inf for _ in range(n)]
    left_dp[0] = a[0]
    right_dp[-1] = a[-1]

    for i in range(n):
        left_dp[i] = min(left_dp[i - 1], a[i])

    for i in range(n - 2, -1, -1):
        right_dp[i] = min(right_dp[i + 1], a[i])

    for i in range(n):
        if a[i] > left_dp[i] and a[i] > right_dp[i]:
            continue

        answer += 1

    return answer
