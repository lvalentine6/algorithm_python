import sys

input = sys.stdin.readline


def calculation(sub_lst):
    result = 0
    i = 0

    while i < len(sub_lst):
        if i + 1 >= len(sub_lst):
            result += sub_lst[i]
            break

        result += sub_lst[i] * sub_lst[i + 1]
        i += 2

    return result


n = int(input())
lst = [int(input()) for _ in range(n)]
lst.sort(reverse=True)
answer = 0

prefix = []
subfix = []
one_cnt = 0
zero_cnt = 0

for l in lst:
    if l == 0:
        zero_cnt += 1
    elif l == 1:
        one_cnt += 1
    elif l > 1:
        prefix.append(l)
    else:
        subfix.append(l)

prefix.sort(reverse=True)
subfix.sort()

while len(subfix) % 2 == 1 and zero_cnt > 0:
    answer -= subfix[-1]
    subfix.pop()
    zero_cnt -= 1

answer = calculation(prefix) + calculation(subfix) + one_cnt

print(answer)
