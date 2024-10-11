from itertools import combinations

n = int(input())

target = list(map(int, input().split()))
lst = [list(map(int, input().split())) for _ in range(n)]

dic = {}

for idx, i in enumerate(lst):
    dic[tuple(i[:-1])] = idx

candidate = []
init_price = 10000

for i in range(1, n+1):
    comb = combinations(lst, i)

    for j in comb:
        m1, m2, m3, m4, price = 0, 0, 0, 0, 0
        idxs = []

        for k in j:
            m1 += k[0]
            m2 += k[1]
            m3 += k[2]
            m4 += k[3]
            price += k[4]
            idxs.append(dic[tuple([k[0], k[1], k[2], k[3]])] + 1)

        if m1 >= target[0] and m2 >= target[1] and m3 >= target[2] and m4 >= target[3] and init_price >= price:
            candidate.append([price, idxs])

if candidate:
    sorted_candidate = sorted(candidate)
    answer = min(sorted_candidate)
    print(answer[0])
    print(*answer[1])
else:
    print('-1')