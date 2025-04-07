import math
import sys
from collections import defaultdict

input = sys.stdin.readline

m, n = list(map(int, input().split()))
lst = defaultdict(int)

for _ in range(m):
    p = list(map(int, input().split()))
    sp = sorted(set(p))
    rank = {v: k for k, v in enumerate(sp)}
    t = tuple(rank[a] for a in p)
    lst[t] += 1

answer = sum(math.comb(v, 2) for v in lst.values())

print(answer)
