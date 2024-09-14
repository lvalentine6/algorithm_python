def solution(s):
    answer = ''

    s = s.lower()
    flag = False
    for i in s:
        if not flag:
            i = i.upper()
            flag = True
        if i == ' ':
            flag = False
        answer += i

    return answer
