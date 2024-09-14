import math


def solution(n, words):
    answer = [0, 0]
    lst = []
    start_char = words[0][0]
    end_char = words[0][-1]
    lst.append(words[0])

    for i in range(1, len(words)):
        if words[i][0] != end_char or words[i] in lst:
            answer = [i % n + 1, math.floor(i / n + 1)]
            break
        start_char = words[i][0]
        end_char = words[i][-1]
        lst.append(words[i])

    return answer
