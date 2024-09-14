from collections import deque


def solution(people, limit):
    answer = 0

    people.sort(reverse=True)
    dq = deque(people)

    while dq:
        temp = dq.popleft()
        if dq and temp + dq[-1] <= limit:
            dq.pop()
        answer += 1

    return answer
