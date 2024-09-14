from itertools import *


def solution(relation):
    answer = 0

    row_size = len(relation)
    col_size = len(relation[0])
    lst = [i for i in range(col_size)]
    keys = []

    comb_lst = []
    for size in range(1, col_size + 2):
        for comb in combinations(lst, size):
            comb_lst.append(set(comb))

    for comb in comb_lst:
        temp_lst = []
        for rel in relation:
            key_str = ''
            for c in comb:
                key_str += rel[c]
            if key_str not in temp_lst:
                temp_lst.append(key_str)

        if len(temp_lst) == row_size:
            flag = False
            for i in range(len(comb)):
                for com in combinations(comb, i):
                    if set(com) in keys:
                        flag = True
                        break
            if not flag:
                keys.append(set(comb))

    answer = len(keys)

    return answer
