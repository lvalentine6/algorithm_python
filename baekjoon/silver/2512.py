import sys

input = sys.stdin.readline

n = int(input())
lst = list(map(int, input().split()))
target = int(input())

if sum(lst) <= target:
    print(max(lst))
else:

    left, right = 1, max(lst)
    answer = 0

    while left <= right:
        mid = (left + right) // 2
        Sum = sum(min(mid, i) for i in lst)

        if Sum <= target:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1

    print(answer)
