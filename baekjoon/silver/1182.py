import sys

input = sys.stdin.readline

n, s = map(int, input().split())
lst = list(map(int, input().split()))

x, y = 0, 0
_sum = 0
answer = 0

while True:
    if _sum >= s or y == n:
        if _sum == s:
            answer += 1
        _sum -= lst[x]
        x += 1
        if x == n:
            break
    else:
        _sum += lst[y]
        y += 1

print(answer)
