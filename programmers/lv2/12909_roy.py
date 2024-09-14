from collections import deque


def solution(s):
    deq = deque()

    for char in s:
        if char == ')' and deq:
            deq.pop()
        else:
            deq.append(char)

    return not deq
