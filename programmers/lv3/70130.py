from collections import Counter


def solution(a):
    answer = 0
    n = len(a)
    counter = Counter(a)

    for v in counter:
        if counter[v] * 2 <= answer:
            continue

        i = 0
        temp = 0
        while i < n - 1:
            if a[i] == a[i + 1]:
                i += 1
                continue
            if v in (a[i], a[i + 1]):
                temp += 1
                i += 2
            else:
                i += 1

        answer = max(answer, temp * 2)

    return answer
