from itertools import *


def solution(numbers, target):
    answer = 0

    elements = ['+', '-']
    size = len(numbers)

    for i in product(elements, repeat=size):
        result = 0
        for j in range(len(numbers)):
            result += int(i[j] + str(numbers[j]))
        if result == target:
            answer += 1

    return answer
