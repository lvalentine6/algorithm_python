def solution(phone_book):
    answer = True

    dic = {i: idx for idx, i in enumerate(phone_book)}

    for num in phone_book:
        temp = ''
        for n in num:
            temp += n
            if temp in dic and temp != num:
                return False

    return answer
