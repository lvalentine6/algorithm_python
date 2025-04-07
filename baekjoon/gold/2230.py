import math
import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))

lst = [int(input()) for _ in range(n)]

lst.sort()

_min = math.inf

left = 0
for right in range(n):
    while left < n and lst[right] - lst[left] >= m:
        _min = min(_min, lst[right] - lst[left])
        left += 1

print(_min)
