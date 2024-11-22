import heapq

INF = int(1e9)


def dijkstra(node):
    distance = [INF] * v
    distance[node] = 0
    queue = []
    heapq.heappush(queue, [0, node])

    while queue:
        pd, pn = heapq.heappop(queue)

        if distance[pn] < pd:
            continue

        for next_node, weight in arr[pn]:
            cost = pd + weight
            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(queue, [cost, next_node])

    return distance


import sys

input = sys.stdin.readline

v, e = map(int, input().split())
k = int(input())
arr = [[] for _ in range(v)]

for i in range(e):
    a, b, w = map(int, input().split())
    arr[a - 1].append((b - 1, w))

result = dijkstra(k - 1)

for re in result:
    if re == INF:
        print('INF')
    else:
        print(re)
