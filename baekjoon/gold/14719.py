import sys

input = sys.stdin.readline

n, m = map(int, input().split())

lst = [[int(j) for j in input().split()] for _ in range(n)]
t_lst = [[int(j) for j in input().split()] for _ in range(m)]

lst.insert(0, [0 for _ in range(n)])

for i in lst:
    i.insert(0, 0)

prefix = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        prefix[i][j] = prefix[i - 1][j] + prefix[i][j - 1] + lst[i][j] - prefix[i - 1][j - 1]

for i in t_lst:
    start_x = i[0]
    start_y = i[1]
    end_x = i[2]
    end_y = i[3]

    if start_x == end_x and start_y == end_y:
        print(lst[start_x][start_y])
    else:
        print(prefix[end_x][end_y] - prefix[start_x - 1][end_y] - prefix[end_x][start_y - 1] + prefix[start_x - 1][
            start_y - 1])
