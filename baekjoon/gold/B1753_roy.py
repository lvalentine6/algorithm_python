import heapq
import sys

inputs = sys.stdin.readline

v, e = map(int, inputs().split())
s = int(inputs())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    u, end, w = map(int, inputs().split())
    graph[u].append((end, w))

inf = float('inf')
distances = [inf] * (v + 1)
distances[s] = 0

queue = [(0, s)]

while queue:
    current_distance, current_vertex = heapq.heappop(queue)
    if distances[current_vertex] < current_distance:
        continue

    for adjacent, weight in graph[current_vertex]:
        distance = current_distance + weight
        if distance < distances[adjacent]:
            distances[adjacent] = distance
            heapq.heappush(queue, (distance, adjacent))

# 출력 부분
for i in range(1, v + 1):
    if distances[i] == inf:
        print("INF")
    else:
        print(distances[i])
