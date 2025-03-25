def rotation(key):
    new_key = [[] for _ in range(len(key))]
    for j in range(len(key)):
        for i in range(len(key) - 1, -1, -1):
            new_key[j].append(key[i][j])

    return new_key


def compare(lst, key, n, m, start_row, start_col):
    tmp = [r[:] for r in lst]

    for k in range(m):
        for r in range(m):
            tmp[start_row + k][start_col + r] += key[k][r]

    for k in range(n):
        for r in range(n):
            if tmp[k + m][r + m] != 1:
                return False

    return True


def solution(key, lock):
    answer = False
    m = len(key)
    n = len(lock)

    lst = [[0 for _ in range(n + 2 * m)] for _ in range(n + 2 * m)]

    for i in range(n):
        for j in range(n):
            lst[i + m][j + m] = lock[i][j]

    for t in range(4):
        for i in range(0, len(lst) - m):
            for j in range(0, len(lst) - m):
                answer = compare(lst, key, n, m, i, j)

                if answer:
                    return answer

        key = rotation(key)

    return answer
