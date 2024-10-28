import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

left = 0
right = max(lst)
answer = 0

while left <= right:
    mid = (left + right) // 2

    tree_sum = sum(tree - mid for tree in lst if tree > mid)

    if tree_sum >= m:
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
