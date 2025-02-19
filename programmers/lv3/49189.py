from collections import deque


def solution(n, edge):
    answer = 0

    vertex = [[] for _ in range(n)]

    for a, b in edge:
        vertex[a - 1].append(b - 1)
        vertex[b - 1].append(a - 1)

    distance = [-1 for _ in range(n)]
    distance[0] = 0

    queue = deque([0])

    while queue:
        position = queue.popleft()
        for v in vertex[position]:
            if distance[v] == -1:
                distance[v] = distance[position] + 1
                queue.append(v)

    _max = max(distance)
    answer = distance.count(_max)

    return answer
