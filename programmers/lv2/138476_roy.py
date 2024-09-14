def solution(k, tangerine):
    answer = 1
    dic = {}

    for i in tangerine:
        if not i in dic:
            dic[i] = 1
        else:
            dic[i] += 1

    sort_dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)

    result = 0
    for i in sort_dic:
        result += i[1]
        if result >= k:
            break
        else:
            answer += 1

    return answer
