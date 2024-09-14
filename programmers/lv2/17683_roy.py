def solution(m, musicinfos):
    answer = "(None)"
    answer_lst = []

    def to_play_minute(s_time, e_time):
        s_hour, s_minute = s_time.split(':')
        e_hour, e_minute = e_time.split(':')
        return (int(e_hour) * 60 + int(e_minute)) - (int(s_hour) * 60 + int(s_minute))

    def to_play_music(info):
        slice_lst = []
        info = list(info[::])

        while len(info) > 0:
            temp = info.pop()
            if temp == '#':
                temp = info.pop() + temp
            slice_lst.append(temp)

        slice_lst = list(slice_lst[::-1])
        return slice_lst

    def to_music():
        result = []
        t = 0
        for i in range(play_minute):
            if i < len(slice_lst):
                result.append(slice_lst[t])
            else:
                t = t % len(slice_lst)
                result.append(slice_lst[t])
            t += 1

        return result

    for idx, infos in enumerate(musicinfos):
        s_time, e_time, title, info = infos.split(',')
        play_minute = to_play_minute(s_time, e_time)
        slice_lst = to_play_music(info)
        m_lst = to_play_music(m)
        music = to_music()

        for i in range(len(music)):
            if ''.join(music[i:i + len(m_lst)]) == ''.join(m_lst):
                answer_lst.append([play_minute, idx, title])

    answer_lst = sorted(answer_lst, key=lambda x: (-x[0], x[1]))

    if answer_lst:
        answer = answer_lst[0][2]

    return answer
