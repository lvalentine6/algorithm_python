import sys

sys.setrecursionlimit(1000000)


def dfs(amounts, graph, name, money):
    if name == "-":
        return

    fee = money // 10
    amounts[name] += money - fee

    dfs(amounts, graph, graph[name], fee)


def solution(enroll, referral, seller, amount):
    answer = [0 for _ in enroll]

    graph = {e: referral[idx] for idx, e in enumerate(enroll)}
    amounts = {e: 0 for e in enroll}

    for idx, s in enumerate(seller):
        dfs(amounts, graph, s, amount[idx] * 100)

    answer = list(amounts.values())

    return answer
