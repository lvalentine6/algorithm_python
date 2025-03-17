def solution(enroll, referral, seller, amount):
    answer = []

    graph = {e: idx for idx, e in enumerate(enroll)}
    parent = [-1 for _ in range(len(enroll))]
    amounts = [0 for _ in range(len(enroll))]

    for idx, name in enumerate(referral):
        if name != "-":
            parent[idx] = graph[name]

    for i in range(len(seller)):
        name = seller[i]
        profit = amount[i] * 100

        while name != "-" and profit > 0:
            idx = graph[name]
            fee = profit // 10
            amounts[idx] += profit - fee

            if parent[idx] == -1:
                break

            name = enroll[parent[idx]]
            profit = fee

    answer = amounts

    return answer
