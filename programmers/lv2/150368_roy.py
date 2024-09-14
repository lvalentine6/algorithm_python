from itertools import *


def solution(users, emoticons):
    answer = []

    discount_rate = [10, 20, 30, 40]
    emoticons_size = len(emoticons)
    discount_lst = []
    result_lst = []

    for per in product(discount_rate, repeat=emoticons_size):
        discount_price = []
        for i in range(len(emoticons)):
            discount_price.append([per[i], emoticons[i] - emoticons[i] * per[i] / 100])
        discount_lst.append(discount_price)

    for i in discount_lst:
        join_num = 0
        max_sell = 0
        for j in users:
            user_sell_amount = 0
            for k in i:
                if k[0] >= j[0]:
                    user_sell_amount += k[1]
            if user_sell_amount >= j[1]:
                join_num += 1
            else:
                max_sell += user_sell_amount
        result_lst.append([join_num, max_sell])

    result_lst.sort(reverse=True)
    answer = result_lst[0]

    return answer
