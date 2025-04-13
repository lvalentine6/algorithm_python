import sys
from collections import deque

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

    dp = [0 for _ in range(n)]

    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)
            dp[i] = times[i]

    while queue:
        cur = queue.popleft()
        for nxt in graph[cur]:
            indegree[nxt] -= 1
            dp[nxt] = max(dp[nxt], dp[cur] + times[nxt])
            if indegree[nxt] == 0:
                queue.append(nxt)

    print(dp[w])

