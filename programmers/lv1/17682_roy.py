def solution(dartResult):
    answer = 0

    lst = list(dartResult)
    score = []
    temp = ''

    dic = {'S': 1, 'D': 2, 'T': 3}

    for idx, char in enumerate(lst):
        if idx > 0 and char.isdigit():
            if temp == '1' and char == '0':
                temp += char
                continue
            score.append(temp)
            temp = ''
        temp += char
    score.append(temp)

    result = []

    for idx, cal in enumerate(score):
        if cal[0] == '1' and cal[1] == '0':
            num = 10
            grade = dic[cal[2]]
        else:
            num = int(cal[0])
            grade = dic[cal[1]]
        num = pow(num, grade)

        if '*' in cal:
            num *= 2
            if idx > 0:
                result[idx - 1] = result[idx - 1] * 2
        if '#' in cal:
            num *= -1
        result.append(num)

    answer = sum(result)
    return answer
