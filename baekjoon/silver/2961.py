from itertools import combinations

n = int(input())
lst = [list(map(int, input().split())) for _ in range(n)]
answer = 1000000000

for i in range(1, n + 1):
    comb = combinations(lst, i)

    for j in comb:
        multi = 1
        plus = 0

        for k in j:
            multi *= k[0]
            plus += k[1]

        answer = min(abs(plus - multi), answer)

print(answer)

