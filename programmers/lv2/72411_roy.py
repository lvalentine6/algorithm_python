from itertools import *


def solution(orders, course):
    answer = []

    for num in course:
        order_dict = {}
        for order in orders:
            memu_lst = list(order)
            for comb in combinations(memu_lst, num):
                comb_sorted = sorted(comb)
                order_dict[tuple(comb_sorted)] = order_dict.get(tuple(comb_sorted), 0) + 1
        if order_dict:
            max_val = max(list(order_dict.values()))
            for k, v in order_dict.items():
                if v == max_val and v > 1:
                    answer.append(''.join(k))

    answer.sort()

    return answer
