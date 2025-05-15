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

def recursion(lst, idx, direction, visited, flag):
    move(lst, idx, direction)
    visited[idx] = True

    if 0 <= idx - 1 and flag[idx - 1]:
        recursion(lst, idx - 1, -1 if direction == 1 else 1, visited, flag)
    if idx + 1 < 4 and flag[idx + 1]:
        recursion(lst, idx + 1, -1 if direction == 1 else 1, visited, flag)


input = sys.stdin.readline
lst = [deque(map(int, input().strip())) for _ in range(4)]
k = int(input())
command = [list(map(int, input().split(' '))) for _ in range(k)]
answer = 0

for i in range(k):
    flag = check(lst)
    idx, direction = command[i]
    idx -= 1
    visited = [False for _ in range(4)]

    move(lst, idx, direction)

    if idx == 0 and flag[0]:
        visited[idx] = True
        recursion(lst, idx + 1, -1 if direction == 1 else 1, visited, flag)
    elif (idx == 1 and flag[0] or flag[1]) or (idx == 2 and flag[1] or flag[2]):
        visited[idx] = True
        recursion(lst, idx + 1, -1 if direction == 1 else 1, visited, flag)
        recursion(lst, idx - 1, -1 if direction == 1 else 1, visited, flag)
    elif idx == 3 and flag[2]:
        visited[idx] = True
        recursion(lst, idx - 1, -1 if direction == 1 else 1, visited, flag)

    print(flag)
    # print(lst)

print(command)
print(lst)

if list(lst[0])[0] == 1:
    answer += 1
if list(lst[1])[0] == 1:
    answer += 2
if list(lst[2])[0] == 1:
    answer += 4
if list(lst[3])[0] == 1:
    answer += 8

print(answer)
