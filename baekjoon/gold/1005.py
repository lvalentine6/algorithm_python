import heapq
import sys

input = sys.stdin.readline
t = int(input())

for _ in range(t):
    n, k = list(map(int, input().split()))
    times = list(map(int, input().split()))
    orders = [list(map(int, input().split())) for _ in range(k)]
    w = int(input()) - 1
    answer = 0

    graph = [[] for _ in range(n)]
    indegree = [0 for _ in range(n)]

    for o in orders:
        a, b = o
        graph[a - 1].append(b - 1)
        indegree[b - 1] += 1

    heap = []

    for i in range(n):
        if indegree[i] == 0:
            heapq.heappush(heap, (times[i], i, indegree[i]))

    p_order = 0

    while heap:
        time, node, ind = heapq.heappop(heap)

        if node == w:
            break

        if p_order == ind:
            answer += time
            p_order += 1

            for nxt in graph[node]:
                indegree[nxt] -= 1
                if indegree[nxt] == 0:
                    heapq.heappush(heap, (times[nxt], nxt, indegree[nxt]))

    print(answer)

