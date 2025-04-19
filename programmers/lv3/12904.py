def solution(s):
    answer = 0
    n = len(s)

    for i in range(n, 0, -1):
        for j in range(n - i + 1):
            split = s[j:j + i]
            if split == split[::-1]:
                answer = i
                return answer

    return answer
