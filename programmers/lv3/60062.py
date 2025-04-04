from itertools import permutations


def solution(n, weak, dist):
    answer = 0
    min_friend = len(dist) + 1

    et_weak = weak + [n + w for w in weak]

    for start in range(len(weak)):
        for friends in permutations(dist):
            cnt = 1
            covered = et_weak[start] + friends[0]

            for i in range(start, start + len(weak)):
                if et_weak[i] > covered:
                    cnt += 1
                    if cnt > len(dist):
                        break
                    covered = et_weak[i] + friends[cnt - 1]

            min_friend = min(min_friend, cnt)

    if min_friend <= len(dist):
        answer = min_friend
    else:
        answer = -1

    return answer