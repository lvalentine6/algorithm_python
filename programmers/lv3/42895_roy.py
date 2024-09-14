def solution(N, number):
    answer = -1

    if N == number:
        return 1

    lst = [set() for _ in range(8)]

    for i in range(8):
        lst[i].add(int(str(N) * (i + 1)))

    for i in range(1, 8):
        for j in range(i):
            for op1 in lst[j]:
                for op2 in lst[i - j - 1]:
                    lst[i].add(op1 + op2)
                    lst[i].add(op1 - op2)
                    lst[i].add(op1 * op2)
                    if op2 != 0:
                        lst[i].add(op1 // op2)

        if number in lst[i]:
            return i + 1

    return answer
