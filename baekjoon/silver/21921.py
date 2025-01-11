import sys

input = sys.stdin.readline

n, x = map(int, input().split())
lst = list(map(int, input().split()))

start = 0
end = x
sum_ = 0
cnt = 1

for i in range(x):
    sum_ += lst[i]

max_ = sum_

while end < n:
    sum_ -= lst[start]
    sum_ += lst[end]
    start += 1
    end += 1
    if sum_ > max_:
        max_ = sum_
        cnt = 1
    elif sum_ == max_:
        cnt += 1

if max_ == 0:
    print('SAD')
else:
    print(max_)
    print(cnt)
