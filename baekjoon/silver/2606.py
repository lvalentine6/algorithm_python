def dfs(num):
    visited[num] = True

    for idx, item in enumerate(network[num]):
        if item == 1 and not visited[idx]:
            dfs(idx)


import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

network = [[0] * n for _ in range(n)]
visited = [False] * n
lst = [list(map(int, input().split())) for _ in range(m)]

for i in lst:
    network[i[0] - 1][i[1] - 1] = 1
    network[i[1] - 1][i[0] - 1] = 1

dfs(0)

print(visited.count(True) - 1)
