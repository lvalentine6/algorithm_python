from itertools import product


def solution(user_id, banned_id):
    answer = 0
    lst = [[] for _ in range(len(banned_id))]
    used = [False for _ in range(len(user_id))]

    for idx, i in enumerate(banned_id):
        ch = list(i)
        for j in user_id:
            uch = list(j)
            flag = False
            for k in range(len(ch)):
                if len(ch) != len(uch):
                    flag = True
                    break
                elif ch[k] != '*' and ch[k] != uch[k]:
                    flag = True
                    break
            if not flag:
                lst[idx].append(j)

    result = set()

    for i in product(*lst):
        if len(set(i)) == len(banned_id):
            result.add(tuple(sorted(i)))

    answer = len(result)

    return answer
