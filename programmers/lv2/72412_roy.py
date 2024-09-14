import re
from bisect import bisect_left
from collections import defaultdict
from itertools import product


def solution(info, query):
    answer = []

    dic = defaultdict(list)
    for i in info:
        temp = i.split()
        part = temp[:-1]
        score = int(temp[-1])

        combination = list(product(*[(p, '-') for p in part]))
        for k in combination:
            key = ':'.join(k)
            dic[key].append(score)

    for y in dic.values():
        y.sort()

    for q in query:
        temp = re.split(' and | ', q)
        sc = int(temp[-1])
        temp = temp[:-1]
        p = ':'.join(temp)

        result = dic[p]
        idx = bisect_left(result, sc)
        answer.append(len(result) - idx)

    return answer
