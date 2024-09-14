def solution(s):
    answer = ''

    sp = s.split(' ')

    for word in sp:
        for idx, char in enumerate(word):
            if idx % 2 == 0:
                answer += char.upper()
                continue
            answer += char.lower()
        answer += ' '
    answer = answer[:-1]
    return answer
