def solution(N, stages):
    answer = []

    people = len(stages)
    lst = []

    for idx in range(1, N + 1):
        cnt = stages.count(idx)
        if cnt == 0:
            lst.append((idx, 0))
            continue
        lst.append((idx, cnt / people))
        people -= cnt

    lst.sort(key=lambda x: (-x[1], x[0]))
    print(lst)

    for i in range(len(lst)):
        answer.append(lst[i][0])

    return answer
