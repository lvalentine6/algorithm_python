import sys

input = sys.stdin.readline

x = int(input())
lst = [64]

while sum(lst) > x:
        tmp = lst.pop(0)
        tmp //= 2
        if tmp + sum(lst) >= x:
            lst.insert(0, tmp)
        else:
            lst.insert(0, tmp)
            lst.insert(0, tmp)

print(len(lst))