def check_t(lst, x, y, c):
    if y == 0:
        if c == 1:
            lst[x][y][0] = 1
        else:
            lst[x][y][0] = 0
    else:
        if x - 1 >= 0 and lst[x - 1][y][1] == 1:
            if c == 1:
                lst[x][y][0] = 1
            else:
                lst[x][y][0] = 0
        elif y - 1 >= 0 and lst[x][y - 1][0] == 1:
            if c == 1:
                lst[x][y][0] = 1
            else:
                lst[x][y][0] = 0
    return lst


def check_f(lst, x, y, c):
    if x - 1 >= 0:
        if lst[x - 1][y][1] == 1 and lst[x + 1][y][1] == 1:
            if c == 1:
                lst[x][y][1] = 1
        elif lst[x][y - 1][0] == 1:
            if c == 1:
                lst[x][y][1] = 1
            else:
                lst[x][y][1] = 0
        if lst[x + 1][y - 1][0] == 1:
            if c == 1:
                lst[x][y][1] = 1
            else:
                lst[x][y][1] = 0
    else:
        if lst[x][y - 1][0] == 1:
            if c == 1:
                lst[x][y][1] = 1
            else:
                lst[x][y][1] = 0

    return lst


def solution(n, build_frame):
    answer = []
    lst = [[[-1, -1] for _ in range(n + 1)] for _ in range(n + 1)]

    for x, y, t, c in build_frame:
        if t == 0:
            lst = check_t(lst, x, y, c)
        else:
            lst = check_f(lst, x, y, c)

    for i in range(n + 1):
        for j in range(n + 1):
            if lst[i][j][0] == 1:
                answer.append([i, j, 0])

            if lst[i][j][1] == 1:
                answer.append([i, j, 1])

    answer.sort(key=lambda x: (x[0], x[1], x[2]))

    return answer
