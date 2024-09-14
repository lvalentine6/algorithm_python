import re


def solution(new_id):
    answer = ''

    new_id = new_id.lower()
    lst = []
    lst2 = []

    for i in new_id:
        if re.match(r'[0-9a-z-_.]', i):
            lst.append(i)

    for i in range(len(lst) - 1):
        if lst[i] == '.' and lst[i + 1] == '.':
            continue
        lst2.append(lst[i])

    if lst and not lst[-1] == '.':
        lst2.append(lst[-1])

    if lst2 and lst2[0] == '.':
        lst2.pop(0)

    if not lst2:
        lst2.append('a')

    if len(lst2) > 15:
        lst2 = lst2[:15]

    if lst2[-1] == '.':
        lst2.pop(-1)

    if len(lst2) <= 2:
        while len(lst2) < 3:
            lst2.append(lst2[-1])
    answer = ''.join(lst2)
    return answer
