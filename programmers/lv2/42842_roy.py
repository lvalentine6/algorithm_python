def solution(brown, yellow):
    answer = []

    lst = list()
    size = brown + yellow

    for i in range(1, size + 1):
        j = int(size / i)
        if i >= j and size % i == 0:
            lst.append([i, j])

    for i, n in enumerate(lst):
        if n[0] * 2 + (n[1] - 2) * 2 == brown:
            answer = lst[i]

    return answer
