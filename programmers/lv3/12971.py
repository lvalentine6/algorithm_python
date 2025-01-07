def solution(sticker):
    answer = 0
    size = len(sticker)

    if size == 1:
        return sticker[0]

    dp1 = [0 for _ in range(size)]
    dp2 = [0 for _ in range(size)]

    dp1[0] = sticker[0]
    dp1[1] = sticker[0]

    for i in range(2, size - 1):
        dp1[i] = max(dp1[i - 1], dp1[i - 2] + sticker[i])

    dp2[0] = 0
    dp2[1] = sticker[1]

    for i in range(2, size):
        dp2[i] = max(dp2[i - 1], dp2[i - 2] + sticker[i])

    print(dp1)
    answer = max(dp1[size - 2], dp2[size - 1])

    return answer
