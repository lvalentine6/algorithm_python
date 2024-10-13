n = int(input())
lst = [int(i) for i in input().split()]

prefix = [lst[0]]

for i in range(1, n):
    prefix.append(max(lst[i] + prefix[i - 1], lst[i]))

print(max(prefix))
