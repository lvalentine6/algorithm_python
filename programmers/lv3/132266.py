from collections import deque


def solution(n, roads, sources, destination):
    answer = []

    lst = [[] for _ in range(n)]
    result = [-1 for _ in range(n)]

    for r in roads:
        lst[r[0] - 1].append(r[1] - 1)
        lst[r[1] - 1].append(r[0] - 1)

    queue = deque()
    queue.append(destination - 1)
    result[destination - 1] = 0

    while queue:
        position = queue.popleft()

        route = lst[position]

        for i in route:
            if result[i] == -1:
                queue.append(i)
                result[i] = result[position] + 1

    for s in sources:
        answer.append(result[s - 1])

    return answer
