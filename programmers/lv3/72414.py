def convert_to_sec(time):
    h, m, s = list(map(int, time.split(':')))
    return h * 60 * 60 + m * 60 + s


def convert_to_hour(time):
    m = time // 60
    s = time % 60
    h = m // 60
    m = m % 60

    return f"{h:02d}:{m:02d}:{s:02d}"


def calculate(lst):
    result = 0
    for v, cnt in lst:
        result += v * cnt

    return result


def solution(play_time, adv_time, logs):
    answer = ''

    lst = []
    play_time_sec = convert_to_sec(play_time)
    adv_time_sec = convert_to_sec(adv_time)
    prefix = [0 for _ in range(play_time_sec + 1)]

    for i in range(len(logs)):
        split = logs[i].split('-')
        start = convert_to_sec(split[0])
        end = convert_to_sec(split[1])

        prefix[start] += 1
        prefix[end] -= 1

    for i in range(1, play_time_sec + 1):
        prefix[i] += prefix[i - 1]

    for i in range(1, play_time_sec + 1):
        prefix[i] += prefix[i - 1]

    max_view = prefix[adv_time_sec - 1]
    _max = 0

    for i in range(adv_time_sec, play_time_sec + 1):
        cur = prefix[i] - prefix[i - adv_time_sec]
        if cur > max_view:
            max_view = cur
            _max = i - adv_time_sec + 1

    answer = convert_to_hour(_max)

    return answer
