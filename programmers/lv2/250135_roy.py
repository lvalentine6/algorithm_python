def solution(h1, m1, s1, h2, m2, s2):
    def hms_to_sec(h, m, s):
        return h * 3600 + m * 60 + s

    def count_alarm(time):
        h_alarm = time * 719 // 43200
        m_alarm = time * 59 // 3600
        penalty = 2 if time >= 43200 else 1
        return h_alarm + m_alarm - penalty

    def alarm_now(time):
        return time * 719 % 43200 == 0 or time * 59 % 3600 == 0

    start_sec = hms_to_sec(h1, m1, s1)
    end_sec = hms_to_sec(h2, m2, s2)

    return count_alarm(end_sec) - count_alarm(start_sec) + (1 if alarm_now(start_sec) else 0)
