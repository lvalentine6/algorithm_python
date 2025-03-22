import math


def solution(scores):
    answer = 1
    n = len(scores)

    sorted_s = sorted(scores, key=lambda x: (-x[0], x[1]))
    lst = []
    max_b = -math.inf
    wan_score = sum(scores[0])

    for a, b in sorted_s:
        if b < max_b:
            if scores[0][0] == a and scores[0][1] == b:
                return -1
            continue
        else:
            lst.append(a + b)
            max_b = max(max_b, b)

    for r in lst:
        if r > wan_score:
            answer += 1

    return answer
