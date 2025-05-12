from itertools import combinations

n = int(input())

decreasing_numbers = []

for i in range(1, 11):
    for comb in combinations(range(10), i):
        decreasing_numbers.append(int(''.join(map(str, sorted(comb, reverse=True)))))

decreasing_numbers.sort()

if n >= len(decreasing_numbers):
    print(-1)
else:
    print(decreasing_numbers[n])
