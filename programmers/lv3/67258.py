def solution(gems):
    n = len(gems)
    size = len(set(gems))

    cnt = {}
    start = 0
    end = 0
    answer = [1, n]

    while end < n:
        cnt[gems[end]] = cnt.get(gems[end], 0) + 1
        end += 1

        while len(cnt) == size:
            if end - start < answer[1] - answer[0] + 1:
                answer = [start + 1, end]

            cnt[gems[start]] -= 1
            if cnt[gems[start]] == 0:
                del cnt[gems[start]]
            start += 1

    return answer
