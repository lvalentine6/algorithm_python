import sys

sys.setrecursionlimit(1000000)

input = sys.stdin.readline


def _union(a, b):
    a = _find(a)
    b = _find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


def _find(a):
    if parent[a] != a:
        parent[a] = _find(parent[a])

    return parent[a]


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for i in range(m):
    cal, a, b = map(int, input().split())

    if cal == 0:
        _union(a, b)
    else:
        if _find(a) == _find(b):
            print("YES")
        else:
            print("NO")

print(parent)