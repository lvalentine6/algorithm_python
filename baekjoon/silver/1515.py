import sys

lst = sys.stdin.readline().strip()

n = 0
while len(lst):
    n += 1
    num = str(n)
    while len(num) and len(lst):
        if num[0] == lst[0]:
            lst = lst[1:]
        num = num[1:]
print(n)
