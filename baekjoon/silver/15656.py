import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))


def recursion(n, m, lst, comb, depth):
    if depth == m:
        print(' '.join(map(str, comb)))
        return

    for i in range(n):
        recursion(n, m, lst, comb + [lst[i]], depth + 1)


recursion(n, m, lst, [], 0)
