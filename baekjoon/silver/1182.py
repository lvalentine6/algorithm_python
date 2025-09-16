import sys
from itertools import combinations

input = sys.stdin.readline

n, s = list(map(int, input().split()))
lst = list(map(int, input().split()))
answer = 0

for i in range(1, n + 1):
    comb = combinations(lst, i)
    for j in comb:
        _sum = sum(j)
        if _sum == s:
            answer += 1

print(answer)
