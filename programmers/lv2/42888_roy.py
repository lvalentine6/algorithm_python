from collections import defaultdict


def solution(record):
    answer = []
    nick_dic = defaultdict(str)

    status_lst = []
    for m in record:
        parts = m.split()
        action, user_id = parts[0], parts[1]
        if action in ['Enter', 'Change']:
            nick_dic[user_id] = parts[2]
        if action != 'Change':
            status_lst.append((action, user_id))

    for action, user_id in status_lst:
        if action == 'Enter':
            message = f'{nick_dic[user_id]}님이 들어왔습니다.'
        elif action == 'Leave':
            message = f'{nick_dic[user_id]}님이 나갔습니다.'
        answer.append(message)

    return answer
