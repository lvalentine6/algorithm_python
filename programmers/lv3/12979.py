import math


def solution(n, stations, w):
    answer = 0
    prev = 0

    for station in stations:
        gap = station - w - 1 - prev
        if gap > 0:
            answer += math.ceil(gap / (2 * w + 1))
        prev = station + w

    if prev < n:
        gap = n - prev
        answer += math.ceil(gap / (2 * w + 1))

    return answer
