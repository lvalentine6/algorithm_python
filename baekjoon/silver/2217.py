import sys

input = sys.stdin.readline

n = int(input())
lst = [int(input()) for _ in range(n)]
answer = 0

lst.sort(reverse=True)

for i in range(n):
    answer = max(answer, lst[i] * (i + 1))

print(answer)
