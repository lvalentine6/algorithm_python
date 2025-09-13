import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline
n = int(input())
lst = [int(input().strip()) for _ in range(n)]
_max = 0


def recursion(lst, _sum, idx, r):
    global _max
    if idx > n - 1:
        _max = max(_sum, _max)
        return

    _sum += lst[idx]

    if r == 1:
        recursion(lst, _sum, idx + 2, 0)
    else:
        recursion(lst, _sum, idx + 1, r + 1)


for i in range(n):
    recursion(lst, 0, i, 0)

print(_max)
