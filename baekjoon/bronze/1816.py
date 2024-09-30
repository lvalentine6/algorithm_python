import math

n = int(input())
input_lst = [int(input()) for i in range(n)]

limit = int(math.pow(10, 6))

for number in input_lst:

    for i in range(2, limit + 1):
        if number % i == 0:
            print('NO')
            break

        if i == limit:
            print('YES')


