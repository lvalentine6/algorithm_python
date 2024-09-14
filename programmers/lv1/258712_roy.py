def solution(friends, gifts):
    answer = 0

    dic = {i: {j: 0 for j in friends if not i == j} for i in friends}
    gift_score = {i: 0 for i in friends}
    result = {i: 0 for i in friends}

    for gift in gifts:
        lst = gift.split(' ')
        dic[lst[0]][lst[1]] += 1
        gift_score[lst[0]] += 1
        gift_score[lst[1]] -= 1

    for i in dic:
        now = dic[i]
        for target in now:
            if now[target] > 0 and now[target] > dic[target][i]:
                result[i] += 1
            elif (now[target] == 0 and dic[target][i] == 0) or now[target] == dic[target][i]:
                if gift_score[i] > gift_score[target]:
                    result[i] += 1

    answer = max(result.values())

    return answer
