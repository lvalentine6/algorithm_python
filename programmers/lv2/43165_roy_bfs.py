from collections import deque


def solution(numbers, target):
    answer = 0
    queue = deque([(0, 0)])

    while queue:
        idx, cur_sum = queue.popleft()

        if idx == len(numbers):
            if cur_sum == target:
                answer += 1
        else:
            queue.append((idx + 1, cur_sum + numbers[idx]))
            queue.append((idx + 1, cur_sum - numbers[idx]))

    return answer
