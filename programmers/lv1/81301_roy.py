def solution(s):
    answer = 0

    lst = list(s)
    dic = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5
        , 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}
    a = ''
    temp = ''

    for i in range(len(s)):
        if not lst[i].isdigit():
            temp += ''.join(lst[i])
            if temp in dic:
                a += str(dic.get(temp))
                temp = ''
        else:
            a += lst[i]
    answer = int(a)

    return answer
