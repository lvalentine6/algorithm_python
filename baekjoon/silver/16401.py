import sys

input = sys.stdin.readline
m, n = list(map(int, input().split()))
lst = list(map(int, input().split()))
answer = 0

left = 1
right = max(lst)

while left <= right:
    mid = (left + right) // 2
    total = 0

    for i in lst:
        total += i // mid

    if total >= m:
        left = mid + 1
        answer = max(answer, mid)
    else:
        right = mid - 1

print(answer)
