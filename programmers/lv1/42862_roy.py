def solution(n, lost, reserve):
    answer = 0

    l_lst = list(set(lost) - set(reserve))
    r_lst = list(set(reserve) - set(lost))

    l_lst.sort()
    r_lst.sort()

    answer = n - len(l_lst)

    for idx in l_lst:
        if idx - 1 in r_lst:
            r_lst.remove(idx - 1)
            answer += 1
        elif idx + 1 in r_lst:
            r_lst.remove(idx + 1)
            answer += 1

    return answer
