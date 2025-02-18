def _union(parent, a, b):
    a = _find(parent, a)
    b = _find(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def _find(parent, x):
    if parent[x] != x:
        parent[x] = _find(parent, parent[x])
    return parent[x]


def solution(n, costs):
    answer = 0

    costs.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]

    for cost in costs:
        a, b, c = cost

        if _find(parent, a) != _find(parent, b):
            _union(parent, a, b)
            answer += c

    return answer
