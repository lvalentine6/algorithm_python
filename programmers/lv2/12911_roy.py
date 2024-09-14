def solution(n):
    answer = 0

    n_cnt = bin(n)[2:].count('1')

    flag = False

    while not flag:
        n += 1
        if bin(n)[2:].count('1') == n_cnt:
            flag = True
            answer = n

    return answer
