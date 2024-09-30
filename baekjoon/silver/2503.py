from itertools import permutations

n = int(input())
input_lst = [list(map(int, input().split())) for _ in range(n)]
item_lst = [i for i in range(1, 10)]
answer = 0

per_lst = permutations(item_lst, 3)
for i in per_lst:
    cnt = 0
    for inp in input_lst:
        number_lst = [int(d) for d in str(inp[0])]
        strike = inp[1]
        ball = inp[2]

        strike_cnt = 0
        ball_cnt = 0

        for idx, nl in enumerate(number_lst):
            if nl in i:
                if nl == i[idx]:
                    strike_cnt += 1
                else:
                    ball_cnt += 1

        if strike == strike_cnt and ball == ball_cnt:
            cnt += 1

    if cnt == n:
        answer += 1

print(answer)