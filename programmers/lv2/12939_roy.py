def solution(s):
    answer = ''

    s = [int(i) for i in s.split()]
    answer += str(min(s)) + ' ' + str(max(s))

    return answer
