def solution(id_list, report, k):
    answer = []

    report_cnt = {ids: 0 for ids in id_list}
    report_lst = {ids: [] for ids in id_list}

    for re in report:
        temp = re.split(' ')
        if not temp[1] in report_lst[temp[0]]:
            report_lst[temp[0]].append(temp[1])
            report_cnt[temp[1]] += 1

    for result in report_lst:
        mail_cnt = 0
        for cnt in report_cnt:
            if report_cnt[cnt] >= k:
                if cnt in report_lst[result]:
                    mail_cnt += 1
        answer.append(mail_cnt)

    return answer
