import math
import sys

input = sys.stdin.readline
n, s = list(map(int, input().split()))
lst = list(map(int, input().split()))
answer = math.inf

left = 0
right = 0
cur_sum = 0

for right in range(n):
    cur_sum += lst[right]

    while cur_sum >= s:
        answer = min(answer, right - left + 1)
        cur_sum -= lst[left]
        left += 1

if answer == math.inf:
    answer = 0

print(answer)
