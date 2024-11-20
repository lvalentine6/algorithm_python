import sys
input = sys.stdin.readline

n, x = map(int, input().split())
lst = sorted(list(map(int, input().split())))
answer = 0

lst = [num for num in lst if num != x]
answer += n - len(lst)

left, right = 0, len(lst)-1
while left < right:
    if lst[left] + lst[right] + x/2 >= x:
        answer += 1
        left += 1
        right -= 1
    else:
        left += 1

print(answer)