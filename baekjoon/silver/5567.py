import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
m = int(input())
lst = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
answer = 0

for _ in range(m):
    idx, target = list(map(int, input().split()))
    lst[idx].append(target)
    lst[target].append(idx)

queue = deque()
for node in lst[1]:
    queue.append((0, node))
visited[1] = True

while queue:
    depth, x = queue.popleft()

    if not visited[x]:
        visited[x] = True
        if depth < 2:
            for node in lst[x]:
                queue.append((depth + 1, node))
            answer += 1

print(answer)
