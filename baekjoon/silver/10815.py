import sys

input = sys.stdin.readline

n = int(input())
has_cards = sorted(list(map(int, input().split())))
m = int(input())
target_cards = list(map(int, input().split()))
answer = []

for target in target_cards:
    left = 0
    right = len(has_cards) - 1

    while left <= right:
        mid = (left + right) // 2
        if target == has_cards[mid]:
            answer.append(1)
            break
        elif target < has_cards[mid]:
            right = mid - 1
        else:
            left = mid + 1

    if left > right:
        answer.append(0)

print(*answer)
