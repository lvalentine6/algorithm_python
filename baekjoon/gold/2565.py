import sys

input = sys.stdin.readline

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]

# A 값으로 정렬후 B가 LIS 찾기
sorted_lst = sorted(lst, key=lambda x: x[0])
dp = [1] * n

for i in range(n):
    for j in range(i):
        if sorted_lst[i][1] > sorted_lst[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))
