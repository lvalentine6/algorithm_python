def solution(sequence):
    n = len(sequence)

    pulse1 = [1 if i % 2 == 0 else -1 for i in range(n)]
    pulse2 = [-1 if i % 2 == 0 else 1 for i in range(n)]

    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]
    dp1[0] = sequence[0] * pulse1[0]
    dp2[0] = sequence[0] * pulse2[0]
    answer = max(dp1[0], dp2[0])

    for i in range(1, n):
        dp1[i] = max(sequence[i] * pulse1[i], dp1[i - 1] + sequence[i] * pulse1[i])
        dp2[i] = max(sequence[i] * pulse2[i], dp2[i - 1] + sequence[i] * pulse2[i])
        answer = max(answer, dp1[i], dp2[i])

    return answer
