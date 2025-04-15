import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
orders = [0 for _ in range(n)]
times = [0 for _ in range(n)]
graph = [[] for _ in range(n)]
dp = [0 for _ in range(n)]
answer = 0

for i in range(n):
    tmp = list(map(int, input().split()))
    times[i] = tmp[0]

    for j in tmp[2:]:
        graph[j - 1].append(i)
        orders[i] += 1

queue = deque()
for i in range(n):
    if orders[i] == 0:
        queue.append(i)
        dp[i] = times[i]

while queue:
    cur = queue.popleft()
    for c in graph[cur]:
        orders[c] -= 1
        dp[c] = max(dp[c], dp[cur] + times[c])
        if orders[c] == 0:
            queue.append(c)

print(max(dp))
