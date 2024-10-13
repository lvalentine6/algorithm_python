n = int(input())

lst = sorted([list(map(int, input().split())) for i in range(n)])
prefix = []

present_x = lst[0][0]
present_y = lst[0][1]

for i in range(1, n):
    if lst[i][1] >= present_y:
        prefix.append((lst[i][0] - present_x) * present_y)
        present_x = lst[i][0]
        present_y = lst[i][1]
    else:
        rest_max_height = max(lst[j][1] for j in range(i, n))
        if rest_max_height == lst[i][1]:
            prefix.append(present_y)

            present_x += 1
            present_y = lst[i][1]
            prefix.append((lst[i][0] - present_x) * present_y)

            present_x = lst[i][0]
            present_y = lst[i][1]

prefix.append(present_y)

print(sum(prefix))
