import sys

input = sys.stdin.readline

n, m = map(int, input().split())
p = list(map(int, input().split()))
node = [[] for _ in range(n + 1)]
answer = p[0]

for i in range(m):
    a, b = map(int, input().split())
    node[a].append(b)
    node[b].append(a)

print(node)

def dfs(n, node, position, visited, num):
    if position == 1:
        return num

    for x in node[position]:
        if not visited[x]:
            visited[x] = True
            res = dfs(n, node, x, visited, num)
            if res != 0:
                return res

    return 0

for i in range(2, n + 1):
    visited = [False for _ in range(n + 1)]
    visited[i] = True
    answer += dfs(n, node, i, visited, p[i - 1])

print(answer)
