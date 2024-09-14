def solution(numbers, hand):
    answer = ''

    val = 1
    dic = {}
    for x in range(3):
        for y in range(3):
            dic[val] = [x, y]
            val += 1
    dic[0] = [3, 1]

    left_hand_position = [3, 0]
    right_hand_position = [3, 2]

    for num in numbers:
        if num in [1, 4, 7]:
            answer += 'L'
            left_hand_position = dic[num]
        elif num in [3, 6, 9]:
            answer += 'R'
            right_hand_position = dic[num]
        else:
            target = dic[num]
            ld = cal(left_hand_position, target)
            rd = cal(right_hand_position, target)

            if ld > rd:
                answer += 'R'
                right_hand_position = target
            elif ld < rd:
                answer += 'L'
                left_hand_position = target
            else:
                if hand == 'left':
                    answer += 'L'
                    left_hand_position = target
                else:
                    answer += 'R'
                    right_hand_position = target
    return answer


def cal(now, target):
    return abs(now[0] - target[0]) + abs(now[1] - target[1])
