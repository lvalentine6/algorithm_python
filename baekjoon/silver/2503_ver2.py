import sys
sys.setrecursionlimit(1000000)

def recursion(hint_idx, num):
    global answer

    if num == 1000:
        return

    if hint_idx == n:
        answer += 1
        recursion(0 ,num+ 1)
        return

    if '0' in list(str(num)) or len(list(str(num))) != len(set(str(num))):
        recursion(hint_idx, num + 1)
        return

    hint_num, strike, ball = input_lst[hint_idx]
    num_lst = list(str(num))
    num_strike = 0
    num_ball = 0
    hint_lst = list(str(hint_num))

    for i in range(3):
        if num_lst[i] in hint_lst:
            if num_lst[i] == hint_lst[i]:
                num_strike += 1
            else:
                num_ball += 1

    if num_strike == strike and num_ball == ball:
        recursion(hint_idx + 1, num)
    else:
        recursion(0, num+1)

n = int(input())
input_lst = [list(map(int, input().split())) for _ in range(n)]
answer = 0

recursion(0, 123)
print(answer)