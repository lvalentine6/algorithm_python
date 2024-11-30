import heapq
import sys

input = sys.stdin.readline

v, e = map(int, input().split())
lst = [[] for _ in range(v + 1)]
visited = [False for _ in range(v + 1)]

answer = 0
cnt = 0

for i in range(e):
    a, b, c = map(int, input().split())
    lst[a].append([c, b])
    lst[b].append([c, a])

queue = [[0, 1]]

while queue:
    if cnt == v:
        break

    weight, node = heapq.heappop(queue)

    if not visited[node]:
        visited[node] = True
        answer += weight
        cnt += 1
        for nxt in lst[node]:
            heapq.heappush(queue, nxt)

print(answer)
