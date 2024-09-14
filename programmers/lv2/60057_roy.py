def solution(s):
    answer = 0
    lst = list(s)
    result_lst = []

    for size in range(1, len(s) + 1):
        start_idx = 0
        end_idx = start_idx + size
        part_lst = []
        for _ in range(len(s) + 1):
            sl = slice(start_idx, end_idx)
            if not lst[sl]:
                break
            part_lst.append(lst[sl])
            start_idx += size
            end_idx += size

        cnt = 1
        make_str = ''
        for i in range(1, len(part_lst)):
            now_str = ''.join(part_lst[i])
            pre_str = ''.join(part_lst[i - 1])

            if now_str == pre_str:
                cnt += 1
            else:
                if cnt > 1:
                    make_str += str(cnt) + pre_str
                    cnt = 1
                else:
                    make_str += pre_str
            if i == len(part_lst) - 1:
                if cnt > 1:
                    make_str += str(cnt) + now_str
                    cnt = 1
                else:
                    make_str += now_str

        result_lst.append(make_str)

    result_lst = result_lst[:-1]

    answer = float('inf')
    if len(result_lst) > 1:
        for st in result_lst:
            if len(st) < answer:
                answer = len(st)
    else:
        answer = len(s)

    return answer
