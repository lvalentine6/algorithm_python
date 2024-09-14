def solution(s):
    answer = []
    cnt = 0
    remove = 0

    while s != '1':
        remove += s.count('0')
        s = bin(s.count('1'))[2:]
        cnt += 1

    answer = [cnt, remove]

    return answer
