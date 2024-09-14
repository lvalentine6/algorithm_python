def solution(survey, choices):
    answer = ''
    mid = 4
    dic = {"R": 0, "T": 0, "C": 0, "F": 0, "J": 0, "M": 0, "A": 0, "N": 0}

    for i in range(len(survey)):
        lst = list(survey[i])

        if choices[i] < mid:
            dic[lst[0]] = dic[lst[0]] + abs(choices[i] - mid)
        elif choices[i] > mid:
            dic[lst[1]] = dic[lst[1]] + abs(choices[i] - mid)

    keys = list(dic.keys())

    for i in range(0, len(keys), 2):
        if dic.get(keys[i]) >= dic.get(keys[i + 1]):
            answer += keys[i]
        else:
            answer += keys[i + 1]

    return answer
