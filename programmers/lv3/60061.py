def is_valid(lst):
    for x, y, t in lst:
        if t == 0:
            if y == 0 or (x, y - 1, 0) in lst or (x - 1, y, 1) in lst or (x, y, 1) in lst:
                continue
            return False
        else:
            if (x, y - 1, 0) in lst or (x + 1, y - 1, 0) in lst or ((x + 1, y, 1) in lst and (x - 1, y, 1) in lst):
                continue
            return False

    return True


def solution(n, build_frame):
    answer = [[]]
    lst = set()

    for x, y, t, c in build_frame:
        if c == 1:
            lst.add((x, y, t))
            if not is_valid(lst):
                lst.remove((x, y, t))
        else:
            lst.remove((x, y, t))
            if not is_valid(lst):
                lst.add((x, y, t))

    answer = sorted(lst, key=lambda x: (x[0], x[1], x[2]))

    return answer
