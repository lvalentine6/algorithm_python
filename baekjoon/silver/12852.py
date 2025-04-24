import math
import sys


def recursion(num, sub, depth):
    global answer
    global lst

    if depth > answer:
        return

    if num == 1:
        if depth < answer:
            answer = depth
            lst = sub + [1]

    if num % 3 == 0:
        recursion(num // 3, sub + [num], depth + 1)
    if num % 2 == 0:
        recursion(num // 2, sub + [num], depth + 1)

    recursion(num - 1, sub + [num], depth + 1)


global answer
global lst
answer = math.inf
lst = []
input = sys.stdin.readline
n = int(input())

recursion(n, [], 0)

print(answer)
print(*lst)
