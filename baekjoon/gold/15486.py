import sys

input = sys.stdin.readline
n = int(input())
calendar = [list(map(int, input().split())) for _ in range(n)]
dp = [0 for _ in range(n + 1)]



print(calendar)
