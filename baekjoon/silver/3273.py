import sys

input = sys.stdin.readline

n,x = map(int, input().split())
lst = sorted(list(map(int, input().split())))
answer = 0
remain = 0
left = 0
right = len(lst) - 1

while left < right:
    if lst[right] == x:
        answer += 1
        right -= 1
        continue

    if left == right:
        remain += 1
        break

    capacity = lst[left] + lst[right] + x / 2
    if capacity >= x:
        answer += 1
        left += 1
        right -= 1
    else:
        left += 1
        remain += 1

answer += remain // 3

print(answer)