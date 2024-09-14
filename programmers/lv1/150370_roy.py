def solution(today, terms, privacies):
    answer = []
    input_day = convert_days(today)

    dic = {term.split(' ')[0]: int(term.split(' ')[1]) * 28 for term in terms}

    for idx, privacy in enumerate(privacies):
        start_date, plus_term = privacy.split(' ')
        start_day = convert_days(start_date)
        compare_day = start_day + dic[plus_term]

        if input_day >= compare_day:
            answer.append(idx + 1)

    return answer


def convert_days(days):
    year, month, day = [int(i) for i in days.split('.')]
    return year * 12 * 28 + month * 28 + day
