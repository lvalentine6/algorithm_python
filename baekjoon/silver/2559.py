n, k = map(int, input().split())
lst = [int(i) for i in input().split()]

prefix = [0 for _ in range(n + 1)]

for i in range(n):
    prefix[i + 1] = lst[i] + prefix[i]

answer = []

for start in range(n + 1 - k):
    end = start + k
    answer.append(prefix[end] - prefix[start])

print(max(answer))
