import heapq


def solution(n, t, m, timetable):
    answer = ''
    result = 0

    s_lst = []
    b_lst = []
    start_bus_time = 9 * 60

    for bt in range(n):
        b_lst.append(start_bus_time)
        start_bus_time += t

    for tt in timetable:
        mm, s = list(map(int, tt.split(':')))
        heapq.heappush(s_lst, mm * 60 + s)

    last_bus = b_lst[-1]

    for i in b_lst:
        cnt = 0
        rest_lst = []
        while s_lst and s_lst[0] <= i and cnt < m:
            rest_lst.append(heapq.heappop(s_lst))
            cnt += 1

        if i == last_bus:
            if cnt < m:
                result = last_bus
            elif cnt == m:
                result = rest_lst[-1] - 1

    hour = str(result // 60)
    minute = str(result % 60)
    delimiter = ":"

    if len(hour) == 1:
        hour = '0' + hour

    if len(minute) == 1:
        minute = '0' + minute

    answer = hour + delimiter + minute

    return answer
