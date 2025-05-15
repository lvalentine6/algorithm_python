import sys
from collections import deque


def check(lst):
    tmp = []
    if lst[0][2] == lst[1][6]:
        tmp.append(False)
    else:
        tmp.append(True)
    if lst[1][2] == lst[2][6]:
        tmp.append(False)
    else:
        tmp.append(True)
    if lst[2][2] == lst[3][6]:
        tmp.append(False)
    else:
        tmp.append(True)

    return tmp


def move(lst, idx, direction):
    if direction == 1:
        tmp = lst[idx].pop()
        lst[idx].appendleft(tmp)
    else:
        tmp = lst[idx].popleft()
        lst[idx].append(tmp)


input = sys.stdin.readline
lst = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())
command = [list(map(int, input().split(' '))) for _ in range(k)]
answer = 0

for i in range(k):
    flag = check(lst)
    idx, direction = command[i]
    idx -= 1
    rotation = [0, 0, 0, 0]
    rotation[idx] = direction

    for i in range(idx - 1, -1, -1):
        if flag[i]:
            rotation[i] = -rotation[i + 1]
        else:
            break

    for i in range(idx + 1, 4):
        if flag[i - 1]:
            rotation[i] = -rotation[i - 1]
        else:
            break

    for idx, d in enumerate(rotation):
        if d != 0:
            move(lst, idx, d)

if list(lst[0])[0] == 1:
    answer += 1
if list(lst[1])[0] == 1:
    answer += 2
if list(lst[2])[0] == 1:
    answer += 4
if list(lst[3])[0] == 1:
    answer += 8

print(answer)
