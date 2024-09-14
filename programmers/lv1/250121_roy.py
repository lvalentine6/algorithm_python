def solution(data, ext, val_ext, sort_by):
    answer = list()

    dic = {'code': 0, 'date': 1, 'maximum': 2, 'remain': 3}

    for node in data:
        if node[dic[ext]] < val_ext:
            answer.append(node)

    answer.sort(key=lambda x: x[dic[sort_by]])

    return answer
