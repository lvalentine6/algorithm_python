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
        last_person = 0
        while s_lst and s_lst[0] <= i and cnt < m:
            last_person = heapq.heappop(s_lst)
            cnt += 1

        if i == last_bus:
            if cnt < m:
                result = last_bus
            else:
                result = last_person - 1

    answer = f"{result // 60:02d}:{result % 60:02d}"

    return answer
