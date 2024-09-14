from itertools import *


def solution(places):
    answer = []

    for place in places:
        people_lst = []
        for rix, row in enumerate(place):
            for cix, col in enumerate(row):
                if col == 'P':
                    people_lst.append([rix, cix])

        check_lst = []
        for comb in combinations(people_lst, 2):
            if abs(comb[0][0] - comb[1][0]) + abs(comb[0][1] - comb[1][1]) <= 2:
                check_lst.append([comb[0], comb[1]])

        status = 1
        for c1, c2 in check_lst:
            if c1[0] == c2[0]:
                if place[c1[0]][c1[1] + 1] != 'X':
                    status = 0
                    break
            elif c1[1] == c2[1]:
                if place[c1[0] + 1][c1[1]] != 'X':
                    status = 0
                    break
            else:
                if c1[1] < c2[1]:
                    if place[c2[0]][c2[1] - 1] != 'X' or place[c1[0] + 1][c1[1]] != 'X':
                        status = 0
                        break
                else:
                    if place[c1[0]][c1[1] - 1] != 'X' or place[c2[0]][c2[1] + 1] != 'X':
                        status = 0
                        break

        answer.append(status)

    return answer
