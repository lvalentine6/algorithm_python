import math


def solution(fees, records):
    answer = []

    basic_time, basic_fee, unit_time, unit_fee = fees
    int(basic_time)
    int(basic_fee)
    int(unit_time)
    int(unit_fee)
    fee_dic = {}

    def convert(time):
        hour, minute = time.split(':')
        return int(hour) * 60 + int(minute)

    def amount_fee(time):
        if time <= basic_time:
            return basic_fee
        else:
            return basic_fee + math.ceil((time - basic_time) / unit_time) * unit_fee

    for record in records:
        time, num, status = record.split()
        convert_time = convert(time)

        if status == 'IN':
            if num in fee_dic:
                added_time = fee_dic[num][2]
                fee_dic[num] = [convert_time, 0, added_time]
            else:
                fee_dic[num] = [convert_time, 0, 0]
        else:
            temp = fee_dic[num][2]
            fee_dic[num] = [-1, 0, convert_time - fee_dic[num][0] + temp]

    for fee in fee_dic.values():
        if fee[0] != -1:
            fee[2] = fee[2] + (23 * 60 + 59) - fee[0]
            fee[0] = 0

    sorted_dic = sorted(fee_dic.keys())
    result_dic = {k: fee_dic[k] for k in sorted_dic}

    for i in result_dic.values():
        answer.append(amount_fee(i[2]))

    return answer
