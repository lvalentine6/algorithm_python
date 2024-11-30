import sys


def _union(x, y):
    x = _find(x)
    y = _find(y)

    if x == y:
        return

    if rank[x] < rank[y]:
        parent[x] = y
    elif rank[y] < rank[x]:
        parent[y] = x
    else:
        parent[x] = y
        rank[y] += 1


def _find(x):
    while parent[x] != x:
        x = parent[x]
    return x


input = sys.stdin.readline

v, e = map(int, input().split())
link = [list(map(int, input().split())) for _ in range(e)]
link.sort(key=lambda x: x[2])
parent = [i for i in range(v + 1)]
rank = [0 for _ in range(v + 1)]
answer = 0

for i in range(e):
    a = link[i][0]
    b = link[i][1]
    weight = link[i][2]

    a = _find(a)
    b = _find(b)

    if a == b:
        continue
    else:
        _union(a, b)
        answer += weight

print(answer)
