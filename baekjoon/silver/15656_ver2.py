import sys
from itertools import product

input = sys.stdin.readline

n, m = map(int, input().split())
lst = sorted(list(map(int, input().split())))

pr = product(lst, repeat=m)

for p in pr:
    print(*p)
