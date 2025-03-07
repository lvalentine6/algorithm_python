from collections import defaultdict


def dfs(lst, position, direction, ticket_size, depth):
    if ticket_size == depth:
        answer.append(direction)
        return

    for move in lst[position]:
        if not move[1]:
            move[1] = True
            dfs(lst, move[0], direction + [move[0]], ticket_size, depth + 1)
            move[1] = False


def solution(tickets):
    global answer
    answer = []

    lst = defaultdict(list)
    for t in tickets:
        tmp = [t[1], False]
        lst[t[0]].append(tmp)

    dfs(lst, 'ICN', ['ICN'], len(tickets), 0)
    answer.sort()

    return answer[0]
