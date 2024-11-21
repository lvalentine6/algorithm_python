def dfs(num):
    visited[num] = True

    for item in network[num]:
        if not visited[item]:
            dfs(item)


import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

network = [[] for _ in range(n)]
visited = [False] * n

for _ in range(m):
    a, b = map(int, input().split())
    network[a-1].append(b-1)
    network[b-1].append(a-1)

dfs(0)

print(visited.count(True) - 1)
